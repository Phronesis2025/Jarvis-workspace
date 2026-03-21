"""
Content Acquisition Layer — GitHub handler.

Fetches README or issue body from public GitHub repos.
Uses GitHub API (no auth) or raw URLs.
"""

from urllib.parse import urlparse

from acquisition.handlers.base import HandlerResult, BaseHandler


def _parse_github_url(url: str) -> tuple[str, str] | tuple[str, str, int] | None:
    """
    Parse GitHub URL into (owner, repo) or (owner, repo, issue_num).

    Returns:
        (owner, repo) for repo/README URLs
        (owner, repo, issue_num) for issue URLs
        None if not a valid GitHub URL
    """
    parsed = urlparse(url)
    if "github.com" not in parsed.netloc.lower():
        return None

    path = parsed.path.strip("/")
    parts = path.split("/")
    if len(parts) < 2:
        return None

    owner, repo = parts[0], parts[1]
    # Remove .git suffix
    if repo.endswith(".git"):
        repo = repo[:-4]

    if len(parts) >= 4 and parts[2] == "issues" and parts[3].isdigit():
        return (owner, repo, int(parts[3]))

    return (owner, repo)


class GitHubHandler(BaseHandler):
    """Handler for GitHub repos (README) and issues."""

    def fetch(self, url: str) -> HandlerResult:
        """Fetch README or issue body from GitHub."""
        parsed = _parse_github_url(url)
        if not parsed:
            raise ValueError(f"Could not parse GitHub URL: {url}")

        if len(parsed) == 3:
            owner, repo, issue_num = parsed
            return self._fetch_issue(owner, repo, issue_num, url)
        else:
            owner, repo = parsed
            return self._fetch_readme(owner, repo, url)

    def _fetch_readme(self, owner: str, repo: str, source_url: str) -> HandlerResult:
        """Fetch README via GitHub API (no auth for public repos)."""
        try:
            return self._fetch_readme_api(owner, repo, source_url)
        except Exception:
            return self._fetch_readme_raw(owner, repo, source_url)

    def _fetch_readme_api(self, owner: str, repo: str, source_url: str) -> HandlerResult:
        """Fetch README via GitHub API."""
        from urllib.request import urlopen, Request

        api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
        req = Request(api_url, headers={"Accept": "application/vnd.github.raw"})
        with urlopen(req, timeout=15) as resp:
            raw_content = resp.read().decode("utf-8", errors="replace")

        metadata = {"repo": f"{owner}/{repo}", "source": "readme", "url": source_url}

        return HandlerResult(
            raw_content=raw_content,
            metadata=metadata,
            raw_content_format="markdown",
            handler_hint="readme",
        )

    def _fetch_readme_raw(self, owner: str, repo: str, source_url: str) -> HandlerResult:
        """Fallback: fetch from raw.githubusercontent.com."""
        from urllib.request import urlopen, Request

        # Try main, then master
        for branch in ["main", "master"]:
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md"
            try:
                req = Request(raw_url, headers={"User-Agent": "ResearchSwarm/1.0"})
                with urlopen(req, timeout=15) as resp:
                    raw_content = resp.read().decode("utf-8", errors="replace")
                break
            except Exception:
                continue
        else:
            raise ValueError(
                f"README not found for {owner}/{repo}. "
                "Repo may be empty, private, or use a different default branch."
            )

        metadata = {"repo": f"{owner}/{repo}", "source": "readme", "url": source_url}

        return HandlerResult(
            raw_content=raw_content,
            metadata=metadata,
            raw_content_format="markdown",
            handler_hint="readme",
        )

    def _fetch_issue(self, owner: str, repo: str, issue_num: int, source_url: str) -> HandlerResult:
        """Fetch issue body via GitHub API."""
        from urllib.request import urlopen, Request

        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}"
        req = Request(api_url, headers={"Accept": "application/vnd.github+json"})
        with urlopen(req, timeout=15) as resp:
            data = resp.read().decode("utf-8", errors="replace")

        import json
        issue = json.loads(data)

        # Handle pull requests (API returns them as issues)
        if issue.get("pull_request"):
            raise ValueError(
                f"URL points to a pull request, not an issue. "
                "Acquisition currently supports issues only."
            )

        body = issue.get("body") or ""
        title = issue.get("title") or ""

        raw_content = f"# {title}\n\n{body}".strip()

        metadata = {
            "repo": f"{owner}/{repo}",
            "source": "issue",
            "issue_number": issue_num,
            "title": title,
            "url": source_url,
        }

        return HandlerResult(
            raw_content=raw_content,
            metadata=metadata,
            raw_content_format="markdown",
            handler_hint="issue_body",
        )

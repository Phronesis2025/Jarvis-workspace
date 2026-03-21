"""
Content Acquisition Layer — generic article/webpage handler.

Fetches page, extracts main text, collects metadata.
"""

from acquisition.handlers.base import HandlerResult, BaseHandler


class ArticleHandler(BaseHandler):
    """Handler for generic articles and webpages."""

    def fetch(self, url: str) -> HandlerResult:
        """
        Fetch webpage and extract main text content.

        Uses requests + BeautifulSoup when available.
        Falls back to stdlib urllib when not.
        """
        try:
            return self._fetch_with_requests(url)
        except ImportError:
            return self._fetch_with_urllib(url)

    def _fetch_with_requests(self, url: str) -> HandlerResult:
        """Fetch and parse using requests + BeautifulSoup."""
        import requests
        from bs4 import BeautifulSoup

        headers = {
            "User-Agent": "ResearchSwarm/1.0 (acquisition; operator-reviewed)",
            "Accept": "text/html,application/xhtml+xml",
        }
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove script, style, nav
        for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
            tag.decompose()

        # Prefer article/main, fallback to body
        main = soup.find("article") or soup.find("main") or soup.find("body")
        if not main:
            text = soup.get_text(separator="\n", strip=True)
        else:
            text = main.get_text(separator="\n", strip=True)

        # Collapse excessive newlines
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        raw_content = "\n\n".join(lines)

        # Metadata
        title = None
        if soup.title:
            title = soup.title.get_text(strip=True)
        if not title and main:
            h1 = main.find("h1")
            if h1:
                title = h1.get_text(strip=True)

        metadata = {"title": title or url, "url": url}

        return HandlerResult(
            raw_content=raw_content,
            metadata=metadata,
            raw_content_format="plain_text",
            handler_hint="page_text",
        )

    def _fetch_with_urllib(self, url: str) -> HandlerResult:
        """Fallback: fetch with urllib, simple text extraction."""
        from urllib.request import urlopen, Request
        from html.parser import HTMLParser

        req = Request(url, headers={"User-Agent": "ResearchSwarm/1.0"})
        with urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        # Simple tag-stripping extractor
        class TextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.skip = False
                self.text_parts = []

            def handle_starttag(self, tag, attrs):
                if tag.lower() in ("script", "style", "nav"):
                    self.skip = True

            def handle_endtag(self, tag):
                if tag.lower() in ("script", "style", "nav"):
                    self.skip = False

            def handle_data(self, data):
                if not self.skip:
                    s = data.strip()
                    if s:
                        self.text_parts.append(s)

        extractor = TextExtractor()
        extractor.feed(html)
        raw_content = "\n\n".join(extractor.text_parts)

        metadata = {"title": url, "url": url}

        return HandlerResult(
            raw_content=raw_content,
            metadata=metadata,
            raw_content_format="plain_text",
            handler_hint="page_text",
        )

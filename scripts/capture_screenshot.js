/**
 * Capture a screenshot of a URL using Playwright.
 * Must be run from a directory that has Playwright installed (e.g. WCS repo).
 * Usage: node capture_screenshot.js <url> <output_path>
 * Exit 0 on success, 1 on failure.
 */
const url = process.argv[2];
const outputPath = process.argv[3];
if (!url || !outputPath) {
  console.error('Usage: node capture_screenshot.js <url> <output_path>');
  process.exit(1);
}

async function main() {
  let playwright;
  try {
    playwright = require('playwright');
  } catch (_) {
    try {
      playwright = require('@playwright/test');
    } catch (__) {
      console.error('Playwright not found. Install with: npm install playwright');
      process.exit(1);
    }
  }
  const browser = await playwright.chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    const fs = require('fs');
    const dir = require('path').dirname(outputPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    await page.screenshot({ path: outputPath, fullPage: false });
  } finally {
    await browser.close();
  }
}

main().then(() => process.exit(0)).catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});

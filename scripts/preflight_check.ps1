$ErrorActionPreference = "SilentlyContinue"

Write-Host "=== JARVIS PHASE-1 PREFLIGHT CHECK ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1] Python version" -ForegroundColor Yellow
python --version
py --version

Write-Host ""
Write-Host "[2] Node / npm version" -ForegroundColor Yellow
node -v
npm -v

Write-Host ""
Write-Host "[3] WCS repo path exists?" -ForegroundColor Yellow
if (Test-Path "C:\dev\wcsv2.0-new") {
  Write-Host "FOUND: C:\dev\wcsv2.0-new" -ForegroundColor Green
} else {
  Write-Host "MISSING: C:\dev\wcsv2.0-new" -ForegroundColor Red
}

Write-Host ""
Write-Host "[4] package.json exists?" -ForegroundColor Yellow
if (Test-Path "C:\dev\wcsv2.0-new\package.json") {
  Write-Host "FOUND: package.json" -ForegroundColor Green
} else {
  Write-Host "MISSING: package.json" -ForegroundColor Red
}

Write-Host ""
Write-Host "[5] Playwright package present in WCS repo?" -ForegroundColor Yellow
if (Test-Path "C:\dev\wcsv2.0-new\package.json") {
  Select-String -Path "C:\dev\wcsv2.0-new\package.json" -Pattern "playwright|@playwright/test"
} else {
  Write-Host "Cannot check Playwright because package.json is missing." -ForegroundColor Red
}

Write-Host ""
Write-Host "[6] Existing data-testid usage?" -ForegroundColor Yellow
if (Test-Path "C:\dev\wcsv2.0-new\src") {
  Get-ChildItem "C:\dev\wcsv2.0-new\src" -Recurse -Include *.ts,*.tsx,*.js,*.jsx |
    Select-String -Pattern "data-testid" |
    Select-Object -First 20
} else {
  Write-Host "src folder not found." -ForegroundColor Red
}

Write-Host ""
Write-Host "[7] Suggested next commands" -ForegroundColor Yellow
Write-Host "cd C:\dev\wcsv2.0-new"
Write-Host "npm install"
Write-Host "npm run dev"
Write-Host "npm run build"
Write-Host ""
Write-Host "If Playwright is missing, install it in the WCS repo:"
Write-Host "npm install -D @playwright/test"
Write-Host "npx playwright install"

@echo off
if "%1"=="" (
    echo Usage: release.bat ^<version^>
    echo Example: release.bat 1.0.0
    exit /b 1
)

set VERSION=%1

echo Releasing DocPrint v%VERSION%...

echo Adding release workflow...
git add .github/workflows/release.yml
git commit -m "Add automated release workflow" 2>nul || echo Workflow already committed
git push origin main

echo Update version in pyproject.toml and __init__.py to %VERSION%, then press any key to continue...
pause >nul

echo Creating release v%VERSION%...
git add pyproject.toml docprint/__init__.py
git commit -m "Bump version to %VERSION%"
git tag "v%VERSION%"
git push origin main
git push origin "v%VERSION%"

echo Release v%VERSION% initiated!
echo Check GitHub Actions: https://github.com/Varietyz/DocPrint/actions
echo PyPI: https://pypi.org/project/docprint/
pause
@echo off
title XERA GAMES - LocalAvaite Catalog Editor
echo.
echo ========================================
echo   XERA GAMES LLC - PROPRIETARY SOFTWARE
echo   LocalAvaite Catalog Editor v2.0
echo   OPENING THIS FROM THE UNITY EDITOR WILL NOT WORK DUE TO FILE PERMISSION ISSUES WITH PYTHON
echo ========================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Installing/Updating dependencies...
pip install -r requirements.txt --quiet

echo.
echo Launching LocalAvaite Catalog Editor...
echo.
python CatalogEditor.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo Check the error messages above
    pause
)
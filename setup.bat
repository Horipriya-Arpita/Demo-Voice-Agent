@echo off
REM Setup script for Voice Agent on Windows

echo ================================================
echo Voice Agent - Setup Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher from python.org
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/4] Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file from .env.example
    echo.
    echo IMPORTANT: Edit .env file and add your API keys!
) else (
    echo .env file already exists, skipping...
)

echo.
echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your API keys
echo 2. Get API keys from:
echo    - Daily.co: https://dashboard.daily.co
echo    - Deepgram: https://console.deepgram.com
echo    - Groq: https://console.groq.com
echo 3. Run the agent: python -m src.main
echo.
echo ================================================
pause

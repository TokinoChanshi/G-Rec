@echo off
chcp 65001 > nul
setlocal

echo ========================================================
echo        G-Rec (Gemini Reconstruction) Setup
echo        Powered by G-S Protocol
echo ========================================================
echo.

:: 1. Check Python
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.10+
    pause
    exit /b
)

:: 2. Create Venv
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
) else (
    echo [INFO] Virtual environment exists.
)

:: 3. Activate & Install
echo [INFO] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo ========================================================
echo [SUCCESS] G-Rec Environment Ready!
echo.
echo To activate manually:  call venv\Scripts\activate
echo To run manager:        python core/manager.py list
echo ========================================================
echo.
pause

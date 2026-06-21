@echo off
echo ========================================
echo Running Pink Morsel Test Suite
echo ========================================
echo.

REM Step 1: Activate the virtual environment
echo [1/3] Activating virtual environment...
call .venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment.
    echo Make sure .venv exists and is properly set up.
    exit /b 1
)

REM Step 2: Run the test suite
echo [2/3] Running pytest test suite...
pytest test_app.py -v --tb=short
if errorlevel 1 (
    echo ERROR: Tests failed!
    exit /b 1
)

REM Step 3: Success
echo.
echo [3/3] All tests passed! ✅
echo ========================================
exit /b 0
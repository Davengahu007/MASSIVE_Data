@echo off
set "command=%~1"
set "dataset_directory=%~2"

set "PYTHON_PATH=C:\Users\Admin\MASSIVE_Data\venv\Scripts\python.exe"
if not exist "%PYTHON_PATH%" (
    echo Python interpreter not found at %PYTHON_PATH%
    exit /b 1
)

if "%command%"=="translation" (
    %PYTHON_PATH% translation.py -d "%dataset_directory%"
) else if "%command%"=="jsonl_with_test_train_dev" (
    %PYTHON_PATH% jsonl_with_test_train_dev.py -d "%dataset_directory%"
) else if "%command%"=="train_sets" (
    %PYTHON_PATH% train_sets.py -d "%dataset_directory%"
) else if "%command%"=="main" (
    %PYTHON_PATH% main.py -d "%dataset_directory%"
) else (
    echo Unknown command: %command%
    exit /b 1
)

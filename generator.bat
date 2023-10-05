@echo off
set command=%1
shift
set dataset_directory=%1

if "%command%"=="translation" (
    python translation.py -d "%dataset_directory%"
) else if "%command%"=="jsonl_with_test_train_dev" (
    python jsonl_with_test_train_dev.py -d "%dataset_directory%"
) else if "%command%"=="train_sets" (
    python train_sets.py -d "%dataset_directory%"
) else if "%command%"=="main" (
    python main.py -d "%dataset_directory%"
) else (
    echo Unknown command: %command%
    echo Usage: %0 {translation^|jsonl_with_test_train^|train_sets^|main} dataset_directory
    exit /b 1
)

# MASSIVE_Data

## Overview

This project consists of several tasks, each described below. The primary goal is to process translation data from the MASSIVE Dataset. The code is organized into different Python files, each focusing on specific aspects of the tasks.

##  Python3 Development Environment 

### Description
- Set up a new Python3 development environment for this assessment.
- Install all the dependencies that you think will be relevant.
- Build a Python3 project with the structure of projects in PyCharm.
- Import the MASSIVE Dataset mentioned in the Data File above.
- Generate an en-xx.xlsx file for all languages using the id, utt, and annot_utt fields.
- Avoid using recursive algorithms due to their time complexity and memory issues.

### Usage
1. Ensure Python3 is installed on your system.
2. Set up a Python3 development environment (e.g., PyCharm).
3. Install the required dependencies (mention them if specific).
4. Organize your project structure.
5. Import the MASSIVE Dataset into your project.
6. Use the provided code to generate the en-xx.xlsx file.

### Example
# Install virtualenv
```bash
pip install virtualenv
```

# Create a new virtual environment
```bash
virtualenv env
```

# Activate the virtual environment
```bash
source env/bin/activate
```

# Install necessary dependencies
```bash
pip install -r requirements.txt
```


##  Working with Files 

### Description
- Generate separate JSONL files for English (en), Swahili (sw), and German (de) for test, train, and dev respectively.
- Generate a single JSON file showing translations from en to xx with id and utt for all train sets.
- Pretty print the JSON file structure.

### Usage
1. Execute the provided code to accomplish the tasks.
2. Ensure you have the required dataset files in the specified directory.

### Example
Include a brief code example or a step-by-step guide if necessary.

### Notes
Sets Variables: It initializes variables with command-line arguments. command gets the first argument, dataset_directory gets the second, and PYTHON_PATH is set to the path of the Python executable.

Checks Python Path: Verifies if Python is installed at PYTHON_PATH; if not, it exits with an error message.

Executes Command: Depending on command value, it executes a different Python script (translation.py, jsonl_with_test_train_dev.py, train_sets.py, or main.py), passing dataset_directory as a parameter. If command is unrecognized, it provides a usage message and exits.

For example, running .\generator.bat translation "your_directory" will execute translation.py -d "your_directory" using the specified Python interpreter.

## File Structure

- `translation.py`: Handles Task 1.
- `train_sets.py`: Handles generating translations for train sets.
- `main.py`: Combines JSONL files into a single Excel file.
- `jsonl_with_test_train_dev.py`: Manages JSONL files for test, train, and dev.

## Dependencies

- `pandas` for data processing.
- `pycountry` for working with locale codes.
- `numpy` for numerical and mathematical operations 
- `wheel` for packaging and distributing projects
- `pip` for package management
- `openpyxl` for reading and writing Excel files









# MASSIVE_Data

## Overview

This project consists of several tasks, each described below. The primary goal is to process translation data from the MASSIVE Dataset. The code is organized into different Python files, each focusing on specific aspects of the tasks.

##  Python3 Development Environment 

### Description
As a team, we've established a new Python 3 development environment for our assessment. To ensure smooth development, we've installed all the relevant dependencies. Our Python project, structured like projects in PyCharm, is ready to go. We've successfully imported the MASSIVE Dataset mentioned in the data file. Using the 'id,' 'utt,' and 'annot_utt' fields, we've generated an 'en-xx.xlsx' file for all languages. To optimize efficiency and avoid time complexity and memory issues, we've steered clear of using recursive algorithms. 

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
To fulfill the task, you need to create separate JSONL files for the test, train, and dev sets in English (en), Swahili (sw), and German (de). Additionally, generate a single JSON file that shows translations from English to an unspecified language (xx) with IDs and utterances for all train sets. Finally, ensure the JSON file structure is well-formatted and easily readable through pretty printing. This approach will organize the data effectively, making it readily available for analysis or use in machine learning tasks.

### Usage
1. Execute the provided code to accomplish the tasks.
2. Ensure you have the required dataset files in the specified directory.

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

- `pip` for package management
- `pandas` for data processing.
  ```bash
    pip install pandas
  ```
- `pycountry` for working with locale codes.
  ```bash
  pip install pycountry
  ```
- `numpy` for numerical and mathematical operations
  ```bash
  pip install numpy
  ```
- `wheel` for packaging and distributing projects
  ```bash
  pip install wheel
  ```
- `openpyxl` for reading and writing Excel files
  ```bash
  pip install openpyxl
  ```
  - `argparse` used to parse command-line arguments and options
    ```bash
    pip install argparse
    ```
  









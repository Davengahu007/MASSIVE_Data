# MASSIVE_Data

# Project Name (e.g., Translation Data Processing)

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
Include a brief code example or a step-by-step guide if necessary.

### Notes
Mention any additional information or flags that may be required to run the code.

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
Mention any additional information or flags that may be required to run the code.

## File Structure

- `translation.py`: Handles Task 1.
- `train_sets.py`: Handles generating translations for train sets.
- `main.py`: Combines JSONL files into a single Excel file.
- `jsonl_with_test_train_dev.py`: Manages JSONL files for test, train, and dev.

## Dependencies

- `pandas` for data processing.
- `pycountry` for working with locale codes.

## Authors

- [Your Name]

## License

This project is open-source and available under the [MIT License](LICENSE) (if applicable).





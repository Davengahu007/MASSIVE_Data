import json
import os
import glob
import argparse

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset_directory', default='./amazon_massive_dataset/data', help='Path to the dataset directory')
args = parser.parse_args()

dataset_directory = args.dataset_directory

input_folder = './amazon_massive_dataset/data'

output_folder = "output_folder"

languages_to_extract = ["en", "sw", "de"]

"""Create the output folder if it doesn't exist"""
os.makedirs(output_folder, exist_ok=True)

"""Create a dictionary to store output file handles by language and partition"""
output_files = {}
for language in languages_to_extract:
    output_files[language] = {}
    for partition in ["test", "train", "dev"]:
        output_files[language][partition] = None

def get_input_file(language_code):
    """Returns the path to the input file for the given language code."""

    input_file_path = glob.glob(f"{input_folder}/*.jsonl")
    for file_path in input_file_path:
        if language_code in file_path:
            return file_path
    return None

def get_output_file(language, partition):
    """Function to get or create an output file for a specific language and partition"""
    if output_files[language][partition] is None:
        output_file_path = os.path.join(output_folder, language, partition + ".jsonl")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        output_files[language][partition] = open(output_file_path, "a", encoding="utf-8")
    return output_files[language][partition]


def filter_and_extract(data, partition):
    """Function to filter and extract data for a specific partition"""
    if "partition" in data and data["partition"] == partition:
        return True
    return False


for language_code in languages_to_extract:
    input_file_path = get_input_file(language_code)
    if input_file_path is not None:

        """Open the corresponding output files for the language and each partition"""
        output_files_for_language = {}
        for partition in ["test", "train", "dev"]:
            output_files_for_language[partition] = get_output_file(language_code, partition)

        """Read and filter the data, then write it to the corresponding output file"""
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            for line in input_file:
                data = json.loads(line.strip())
                for partition in ["test", "train", "dev"]:
                    if filter_and_extract(data, partition):
                        output_files_for_language[partition].write(json.dumps(data, ensure_ascii=False) + "\n")

        for output_file in output_files_for_language.values():
            output_file.close()

for output_files_for_language in output_files.values():
    for output_file in output_files_for_language.values():
        if output_file is not None:
            output_file.close()
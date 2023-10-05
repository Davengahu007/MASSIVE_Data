import argparse
from jsonl_with_test_train_dev import process_data
from train_sets import create_train_sets
from translation import create_translation

input_folder = './amazon_massive_dataset/data'
output_folder = "output_folder"
languages_to_extract = ["en", "sw", "de"]


"""Argument Parsing"""
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset_directory', default='./amazon_massive_dataset/data', help='Path to the dataset directory')
args = parser.parse_args()

dataset_directory = args.dataset_directory

process_data(input_folder, output_folder, languages_to_extract)

input_directory = './amazon_massive_dataset/data'
output_file = 'translations_train.json'

create_train_sets(dataset_directory, output_file)

dataset_directory = './amazon_massive_dataset/data'

create_translation(dataset_directory)
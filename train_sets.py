import pandas as pd
import json
import os
import argparse

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset_directory', default='./amazon_massive_dataset/data', help='Path to the dataset directory')
args = parser.parse_args()

dataset_directory = args.dataset_directory

input_directory = './amazon_massive_dataset/data'
output_file = 'translations_train.json'

translations = {}

for filename in os.listdir(input_directory):
    if filename.endswith('.jsonl'):
        language_code = filename.split('.')[0]  # Extract language code from the filename
        df = pd.read_json(os.path.join(input_directory, filename), lines=True)
        for index, row in df.iterrows():
            if row['partition'] == 'train':
                translation = row['utt']
                id = row['id']
                if id not in translations:
                    translations[id] = {"id": id, "utt": {}}
                translations[id]["utt"][language_code] = translation

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(translations, json_file, ensure_ascii=False, indent=4)

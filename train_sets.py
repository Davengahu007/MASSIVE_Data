import pandas as pd
import json
import os


def create_train_sets(dataset_directory, output_file):
    translations = {}

    for filename in os.listdir(dataset_directory):
        if filename.endswith('.jsonl'):
            language_code = filename.split('.')[0]
            df = pd.read_json(os.path.join(dataset_directory, filename), lines=True)
            for index, row in df.iterrows():
                if row['partition'] == 'train':
                    translation = row['utt']
                    id = row['id']
                    if id not in translations:
                        translations[id] = {"id": id, "utt": {}}
                    translations[id]["utt"][language_code] = translation

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(translations, json_file, ensure_ascii=False, indent=4)
import pandas as pd
import os

# dataset_directory = 'C:\\Users\\Admin\\MASSIVE_Data\\amazon_massive_dataset\\data'

dataset_directory = './amazon_massive_dataset/data'

dfs = []

for filename in os.listdir(dataset_directory):
    if filename.endswith('.jsonl'):

        df = pd.read_json(os.path.join(dataset_directory, filename), lines=True)

        locale = df['locale'].iloc[0]

        new_df = df[['id']].copy()
        new_df[locale] = df['utt'] + ': ' + df['annot_utt']

        dfs.append(new_df)

final_df = dfs[0]
for df in dfs[1:]:
    final_df = final_df.merge(df, on='id', how='outer')

final_df.to_excel('output.xlsx', index=False)

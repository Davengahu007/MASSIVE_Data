import pandas as pd
import os

# Directory containing your .jsonl files
dataset_directory = 'C:\\Users\\Admin\\MASSIVE_Data\\amazon_massive_dataset\\data'

# Initialize an empty list to collect dataframes
dfs = []

# Loop through each file in the directory
for filename in os.listdir(dataset_directory):
    if filename.endswith('.jsonl'):
        # Read the .jsonl file into a dataframe
        df = pd.read_json(os.path.join(dataset_directory, filename), lines=True)

        # Extracting locale value from the first record (assuming all records have the same locale)
        locale = df['locale'].iloc[0]

        # Create a new dataframe with 'id' and formatted 'utt: annot_utt' column
        new_df = df[['id']].copy()
        new_df[locale] = df['utt'] + ': ' + df['annot_utt']

        dfs.append(new_df)

# Merge all dataframes on the 'id' column
final_df = dfs[0]
for df in dfs[1:]:
    final_df = final_df.merge(df, on='id', how='outer')

# Save to Excel
final_df.to_excel('output.xlsx', index=False)

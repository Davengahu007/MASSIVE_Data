import pandas as pd
import os
import pycountry
def get_language_from_locale(locale):
    try:
        # Split the locale to just get the language part (before the '-')
        language_code = locale.split('-')[0]
        # Return the name of the language
        return pycountry.languages.get(alpha_2=language_code).name
    except AttributeError:
        # Return the locale if the language isn't found (as a fallback)
        return locale

# Directory containing your .jsonl files
dataset_directory = '/Users/Michelle/PycharmProjects/MASSIVE_Data/amazon_massive_dataset/data'
# Read the en-US.jsonl file into a dataframe
english_df = pd.read_json(os.path.join(dataset_directory, 'en-US.jsonl'), lines=True)
english_df['en-US'] = english_df['utt'] + ': ' + english_df['annot_utt']

# Create a new Excel writer object
with pd.ExcelWriter('translation_sheets_by_language.xlsx') as writer:
    # Loop through each file in the directory
    for filename in os.listdir(dataset_directory):
        if filename.endswith('.jsonl') and filename != 'en-US.jsonl':
            # Read the .jsonl file into a dataframe
            df = pd.read_json(os.path.join(dataset_directory, filename), lines=True)

            # Extracting locale value from the first record
            locale = df['locale'].iloc[0]

            # Get the language name for the current locale
            language_name = get_language_from_locale(locale)

            # Create a new dataframe with 'id' and formatted 'utt: annot_utt' column for current language
            df[locale] = df['utt'] + ': ' + df['annot_utt']

            # Merge English dataframe with current language dataframe
            merged_df = english_df[['id', 'en-US']].merge(df[['id', locale]], on='id', how='outer')

            # Write the merged dataframe to a new sheet in the Excel workbook
            merged_df.to_excel(writer, sheet_name=language_name, index=False)

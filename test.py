import pandas as pd
import re

def process_cricket_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Extract the column with merged data
    data = df[df.columns[0]]  # Assume all data is in the first column

    # Prepare lists for structured data
    player_names = []
    ages = []

    # Loop over each row to extract the player's name and age
    for row in data:
        # Use regex to separate name and age
        match = re.match(r"([A-Za-z\s]+)(Age:\s\d+y\s\d+d)", row)
        if match:
            player_names.append(match.group(1).strip())
            ages.append(match.group(2).strip())
        else:
            player_names.append(row.strip())  # In case age data is missing
            ages.append('Age: N/A')

    # Create a new DataFrame with structured columns
    clean_df = pd.DataFrame({
        'Player Name': player_names,
        'Age': ages
    })

    # Overwrite the original CSV with cleaned data
    clean_df.to_csv(file_path, index=False)

# Usage
file_paths = [r'C:\\Users\\Faisal\\Desktop\\Project 1\\10 Players Bio\\Afghanistan_Cricketers.csv', r'C:\\Users\\Faisal\\Desktop\\Project 1\\10 Players Bio\Australia_Cricketers.csv',
             r'C:\\Users\\Faisal\Desktop\\Project 1\\10 Players Bio\\Bangladesh_Cricketers.csv', r'C:\\Users\\Faisal\\Desktop\\Project 1\\10 Players Bio\\England_Cricketers.csv',
             r'C:\\Users\\Faisal\\Desktop\\Project 1\\10 Players Bio\\India_Cricketers.csv',r'C:\\Users\Faisal\Desktop\Project 1\10 Players Bio\Ireland_Cricketers.csv'
             ,r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\New_Zealand_Cricketers.csv',r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Pakistan_Cricketers.csv'
             ,r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\South_Africa_Cricketers.csv',r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Sri_Lanka_Cricketers.csv',
             r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\West_Indies_Cricketers.csv',r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Zimbabwe_Cricketers.csv']

for file_path in file_paths:
    process_cricket_data(file_path)

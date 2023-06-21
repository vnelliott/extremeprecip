#THIS CODE DIDN'T END UP SWTICHING THE LAT AND LON COLUMN ORDER AS DESIRED
#WILL WRITE ANOTHER CODE TO READ THROUGH THE FILES AGAIN TO DO THIS
#GONNA POST THIS ANYWAYS SINCE IT WAS A LITTLE USEFUL

import os
import pandas as pd
from tqdm import tqdm

def process_csv_files(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in tqdm(files, desc="Processing files"):
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                process_csv_file(file_path)

def process_csv_file(file_path):
    df = pd.read_csv(file_path)
    
    # Switch LAT and LON columns
    df['LAT'], df['LON'] = df['LON'], df['LAT']
    
    # Add an empty column titled ELEV before the PRECIP column
    df.insert(df.columns.get_loc('PRECIP'), 'ELEV', '')
    
    # Add an empty column titled NAME after the STATION_ID column
    df.insert(df.columns.get_loc('STATION_ID') + 1, 'NAME', '')
    
    # Save the updated data back to CSV
    df.to_csv(file_path, index=False)

# Specify the root directory where your CSV files are located
root_directory = 'C:/Users/vnell/OneDrive - Texas A&M University/Extreme Precip/CONVERTEDCRN_subhour'

# Call the function to process the CSV files
process_csv_files(root_directory)

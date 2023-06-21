import os
import csv
from tqdm import tqdm

def convert_txt_to_csv(txt_file, headers, output_directory, columns_to_keep):
    csv_file = os.path.splitext(os.path.basename(txt_file))[0] + '.csv'
    year_folder = os.path.basename(os.path.dirname(txt_file))
    year_directory = os.path.join(output_directory, year_folder)

    # Create the year-specific subdirectory if it doesn't exist
    if not os.path.exists(year_directory):
        os.makedirs(year_directory)

    csv_path = os.path.join(year_directory, csv_file)

    with open(txt_file, 'r') as file:
        lines = file.readlines()

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file, escapechar='\\')  # Add escape character '\\'
        writer.writerow(headers)  # Write the header row
        for line in lines:
            row = line.strip().split()
            filtered_row = [row[i] for i in columns_to_keep]
            writer.writerow(filtered_row)

def convert_files_to_csv(directory, output_directory, headers, columns_to_keep):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    file_count = sum(len(files) for _, _, files in os.walk(directory))

    with tqdm(total=file_count, desc='Converting files') as pbar:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    txt_file = os.path.join(root, file)
                    convert_txt_to_csv(txt_file, headers, output_directory, columns_to_keep)
                    pbar.update(1)
                else:
                    print(f"Skipping {file} as it is not a text file.")

# Provide the absolute directory path containing the folders
directory = 'C:/Users/vnell/OneDrive - Texas A&M University/Extreme Precip/CRN_subhour'

# Provide the absolute directory path where the CSV files will be saved
output_directory = 'C:/Users/vnell/OneDrive - Texas A&M University/Extreme Precip/CONVERTEDCRN_subhour'

# Provide the headers manually
headers = [
    'STATION_ID', 'DATE', 'TIME', 'LON', 'LAT', 'PRECIP'
]

# Specify the indices of the columns you want to keep (0-based index)
columns_to_keep = [0, 1, 2, 6, 7, 9]

# Call the function to convert the files
convert_files_to_csv(directory, output_directory, headers, columns_to_keep)



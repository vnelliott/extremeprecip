# WORKING WITH THE TAR FILES
import tarfile # importing the "tarfile" module

file = tarfile.open('us-climate-normals_1991-2020_monthly_multivariate_by-station_c20210609.tar.gz') # open file FOR MONTHLY
file.extractall('./monthly') # extract files
file.close() # close file

file = tarfile.open('us-climate-normals_1991-2020_annualseasonal_multivariate_by-station_c20210609.tar.gz') #open file FOR ANNUAL
file.extractall('./annual') #extract files
file.close() #close file


# DELETEING ALL CSV FILES THAT ARE NOT TEXAS STATIONS
import os
import pandas as pd

directory = "C:/Users/vnelliott/Downloads/monthly" #PROCESS FOR MONTHLY
target_string = "TX US"

for filename in os.listdir(directory): # iterate over files in directory
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        
        df = pd.read_csv(filepath) # read in CSV data
        
        match_found = any(df.apply(lambda x: target_string in str(x), axis=0)) # check if target string is present in any column

        if not match_found: # if no match is found, delete the file
            os.remove(filepath)
            
directory = "C:/Users/vnelliott/Downloads/annual" #PROCESS FOR ANNUAL
target_string = "TX US"

for filename in os.listdir(directory): # iterate over files in directory
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)

        df = pd.read_csv(filepath) # read in CSV data

        match_found = any(df.apply(lambda x: target_string in str(x), axis=0)) # check if target string is present in any column

        if not match_found: # if no match is found, delete the file
            os.remove(filepath)


#MERGING CSV FILES INTO ONE (able to include all columns even if not all files have them)
folder_path = 'C:/Users/vnelliott/Downloads/monthly' #DEFINING PATH FOR MONTHLY FOLDER

merged_df = pd.DataFrame() # Create an empty DataFrame to store the merged data

for filename in os.listdir(folder_path): # Loop through all CSV files in the folder
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(folder_path, filename)) # Load the CSV file into a pandas DataFrame
        
        merged_df = pd.concat([merged_df, df], ignore_index=True) # Merge the DataFrame with the merged_df DataFrame

merged_df.to_csv('monthlymerged.csv', index=False) # Write the merged DataFrame to a new CSV file

folder_path = 'C:/Users/vnelliott/Downloads/annual' #DEFINING PATH FOR ANNUAL FOLDER

merged_df = pd.DataFrame() # Create an empty DataFrame to store the merged data

for filename in os.listdir(folder_path): # Loop through all CSV files in the folder
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(folder_path, filename)) # Load the CSV file into a pandas DataFrame
        
        merged_df = pd.concat([merged_df, df], ignore_index=True) # Merge the DataFrame with the merged_df DataFrame

merged_df.to_csv('annualmerged.csv', index=False) # Write the merged DataFrame to a new CSV file


#DELETEING UNNEEDED COLUMNS
df = pd.read_csv('monthlymerged.csv', usecols=['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'DATE', 'MLY-PRCP-NORMAL']) # Read in the CSV file and keep only needed columns for MONTHLY

df.to_csv('monthly.csv', index=False) # Write the modified dataframe to a new CSV file

df = pd.read_csv('annualmerged.csv', usecols=['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'ANN-SNOW-NORMAL', 'ANN-HTDD-NORMAL', 'DJF-TMIN-NORMAL', 'JJA-TMAX-NORMAL', 'ANN-TMIN-AVGNDS-LSTH032', 'ANN-CLDD-BASE72', 'ANN-TMIN-PRBGSL-T32FP50', 'ANN-TMIN-PRBLST-T32FP10', 'ANN-TMIN-PRBFST-T32FP10', 'ANN-TMIN-PRBFST-T32FP50', 'ANN-PRCP-AVGNDS-GE001HI', 'ANN-SNOW-AVGNDS-GE001TI', 'ANN-SNWD-AVGNDS-GE001WI', 'ANN-TMIN-PRBLST-T32FP50']) # Read in the CSV file and keep only needed columns for ANNUAL

df.to_csv('annual.csv', index=False) # Write the modified dataframe to a new CSV file
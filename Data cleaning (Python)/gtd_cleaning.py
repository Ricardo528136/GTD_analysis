# Importing libraries
import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv('Data\globalterrorismdb_0522dist.csv', encoding='ISO-8859-1', low_memory=False, sep=';')

# Previewing the structure of the dataset
print(df.shape)
print(df.head())
print(df.info())
print(df.columns.values)

# Rename columns for easier access
df.rename(columns={
    'ï»¿eventid': 'event_id',
    'iyear': 'year',
    'imonth': 'month',
    'iday': 'day',
    'country_txt': 'country',
    'region_txt': 'region',
    'provstate': 'state',
    'city': 'city',
    'latitude': 'lat',
    'longitude': 'lon',
    'attacktype1_txt': 'attack_type',
    'targtype1_txt': 'target_type',
    'weaptype1_txt': 'weapon_type',
    'nkill': 'killed',
    'nwound': 'wounded',
    'gname': 'group_name',
    'summary': 'summary',
    'success': 'success',
    'suicide': 'suicide'
}, inplace=True)

# Keep only the relevant columns
columns_to_keep = [
    'event_id', 'year', 'month', 'day', 'country', 'region', 'state', 
    'city', 'lat', 'lon', 'attack_type', 'target_type', 'weapon_type', 
    'killed', 'wounded', 'summary', 'group_name', 'success', 'suicide', 
]
df = df[columns_to_keep]

# Checking for missing values
print(df.isnull().sum())

# Drop rows with missing latitude or longitude (no 1st order administrative region could be identified)
df.dropna(subset=['lat', 'lon'], inplace=True)
df = df[(df['lat'].between(-90, 90)) & (df['lon'].between(-180, 180))]

# Filling missing values in the city and summary column
df['city'].fillna('Unknown', inplace=True)
df['summary'].fillna('Not systematically available before 1997', inplace=True)

# Create binary flags
df['is_suicide'] = df['suicide'].apply(lambda x: True if x == 1 else False)
df['is_success'] = df['success'].apply(lambda x: True if x == 1 else False)

# Create datetime column (unknown days and months will show up as 0)
df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

# Create new feature: total casualties
df['casualties'] = df['killed'] + df['wounded']

# Final preview
print("Cleaned dataset shape", df.shape)
print(df.head())

# Export cleaned data
df.to_csv('Data\gtd_cleaned.csv', index=False)
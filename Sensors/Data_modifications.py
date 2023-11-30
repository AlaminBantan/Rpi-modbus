import pandas as pd

# Assuming your CSV data is in a file named 'climatic_data.csv'
file_path = '/home/cdacea/GH_data/climatic_data.csv'

# Read CSV, skipping rows with non-numeric 'Time'
df = pd.read_csv(file_path, skiprows=lambda x: x == 14, na_values=['Time'])

# Convert 'Time' column to datetime format, handling mixed data types
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce')

# Remove rows where 'Time' couldn't be converted
df = df.dropna(subset=['Time'])

# Round 'Time' to the nearest 15 minutes
df['Time'] = df['Time'].dt.round('15min')

# Group by 'Date', 'Time', 'Zone', and 'Subzone' and calculate the mean for each group
result_df = df.groupby(['Date', 'Time', 'Zone', 'Subzone']).mean().reset_index()

# Save the modified DataFrame to a new CSV file
modified_file_path = '/home/cdacea/GH_data/modified_climatic_data.csv'
result_df.to_csv(modified_file_path, index=False)

print(f"Modified data saved to {modified_file_path}")

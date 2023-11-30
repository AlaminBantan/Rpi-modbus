import pandas as pd

# Assuming your CSV data is in a file named 'climatic_data.csv'
file_path = '/home/cdacea/GH_data/climatic_data.csv'
df = pd.read_csv(file_path)

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Round 'Time' to the nearest 15 minutes
df['Time'] = df['Time'].dt.round('15min')

# Group by 'Date', 'Time', 'Zone', and 'Subzone' and calculate the mean for each group
result_df = df.groupby(['Date', 'Time', 'Zone', 'Subzone']).mean().reset_index()

# Save the modified DataFrame to a new CSV file
modified_file_path = '/home/cdacea/GH_data/modified_climatic_data.csv'
result_df.to_csv(modified_file_path, index=False)

print(f"Modified data saved to {modified_file_path}")

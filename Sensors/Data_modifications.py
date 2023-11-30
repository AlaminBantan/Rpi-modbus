import pandas as pd

# Replace '/home/cdacea/GH_data/climatic_data.csv' with your actual file path
file_path = '/home/cdacea/GH_data/climatic_data.csv'
output_file_path = '/home/cdacea/GH_data/modified_climatic_data.csv'

# Assuming your data is stored in a CSV file
data = pd.read_csv(file_path)

# Convert 'Date' and 'Time' columns to datetime format
data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])

# Group by 'Datetime', 'Zone', and 'Subzone', and calculate the average for each group
grouped_data = data.groupby(['Datetime', 'Zone', 'Subzone']).agg({
    'PAR': 'mean',
    'Solar radiation': 'mean',
    'Temp': 'mean',
    'Humidity': 'mean',
    'CO2 conc': 'mean'
}).reset_index()

# Save the resulting grouped data to a new CSV file
grouped_data.to_csv(output_file_path, index=False)

# Print a message indicating the process is complete
print(f"Modified data saved to {output_file_path}")

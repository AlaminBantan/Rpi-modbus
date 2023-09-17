import pandas as pd

# Read the CSV file
df = pd.read_csv('Light_comparison1.csv')

# Group by Time and aggregate the values
df = df.groupby('Time').agg({
    'PAR Intensity Zone B': 'sum',
    'PAR Intensity Zone C': 'sum',
    'Solar Radiation Zone B': 'sum',
    'Solar Radiation Zone C': 'sum'
}).reset_index()

# Save the updated dataframe to a new CSV file
df.to_csv('updated_Light_comparison1.csv', index=False)
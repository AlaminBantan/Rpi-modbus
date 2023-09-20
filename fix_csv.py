import pandas as pd

# Assuming 'C:\\Users\\bantanam\\Downloads\\Light_comparison.csv' is the file containing your data
df = pd.read_csv('C:\\Users\\bantanam\\Downloads\\Light_comparison.csv')

# Convert 'Date' and 'Time' columns to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

# Create separate columns for date and time
df['Date'] = df['Date'].dt.date
df['Time'] = df['Time'].apply(lambda x: x.strftime('%H:%M'))

# Replace negative values with 0 in specific columns
cols_to_replace = ['PAR Intensity Zone B', 'PAR Intensity Zone C', 'Solar Radiation Zone B', 'Solar Radiation Zone C']
df[cols_to_replace] = df[cols_to_replace].apply(lambda x: x.clip(lower=0))

# Group by minute and aggregate the values
df_minute = df.groupby(['Date', 'Time']).agg({
    'PAR Intensity Zone B': 'mean',
    'PAR Intensity Zone C': 'mean',
    'Solar Radiation Zone B': 'mean',
    'Solar Radiation Zone C': 'mean'
}).reset_index()

# Save the consolidated data as a CSV file
df_minute.to_csv('C:\\Users\\bantanam\\Downloads\\updated_Light_comparison.csv', index=False)

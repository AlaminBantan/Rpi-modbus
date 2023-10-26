import pandas as pd

# Assuming 'C:\\Users\\bantanam\\Downloads\\Light_comparison.csv' is the file containing your data
df = pd.read_csv('C:\\Users\\bantanam\\Downloads\\Light_comparison11.csv')

# Convert 'Date' and 'Time' columns to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

# Create separate columns for date and time
df['Date'] = df['Date'].dt.date
df['Time'] = df['Time'].apply(lambda x: x.strftime('%H:%M'))

# Replace negative values with 0 in specific columns
cols_to_replace = ['PAR Intensity Zone B (1)', 'PAR Intensity Zone C (1)', 'Solar Radiation Zone B (1)', 'Solar Radiation Zone C (1)', 'PAR Intensity Zone B (2)', 'PAR Intensity Zone C (2)', 'Solar Radiation Zone B (2)', 'Solar Radiation Zone C (2)', 'PAR Intensity Zone B (3)', 'PAR Intensity Zone C (3)', 'Solar Radiation Zone B (3)', 'Solar Radiation Zone C (3)']
df[cols_to_replace] = df[cols_to_replace].apply(lambda x: x.clip(lower=0))


# Group by minute and aggregate the values
df_minute = df.groupby(['Date', 'Time']).agg({
    'PAR Intensity Zone B (1)': 'mean',
    'PAR Intensity Zone B (2)': 'mean',
    'PAR Intensity Zone B (3)': 'mean',
    'PAR Intensity Zone C (1)': 'mean',
    'PAR Intensity Zone C (2)': 'mean',
    'PAR Intensity Zone C (3)': 'mean',
    'Solar Radiation Zone B (1)': 'mean',
    'Solar Radiation Zone B (2)': 'mean',
    'Solar Radiation Zone B (3)': 'mean',
    'Solar Radiation Zone C (1)': 'mean',
    'Solar Radiation Zone C (2)': 'mean',
    'Solar Radiation Zone C (3)': 'mean',

}).reset_index()

# Save the consolidated data as a CSV file
df_minute.to_csv('C:\\Users\\bantanam\\Downloads\\Light_comparison_28_September.csv', index=False)

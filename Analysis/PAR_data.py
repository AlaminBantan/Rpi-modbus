import pandas as pd

# Read the CSV file
df = pd.read_csv('/home/cdacea/GH_data/modified_data_15min.csv')

# Extract relevant columns
df_extracted = df[['RoundedDateTime', 'Zone', 'Subzone', 'PAR']]

# Pivot the table to have zones and subzones as columns
df_pivoted = df_extracted.pivot_table(index=['RoundedDateTime'], columns=['Zone', 'Subzone'], values='PAR')

# Calculate mean values for each zone
df_pivoted['Mean zone B'] = (df_pivoted[('B', 1)] + df_pivoted[('B', 2)]) / 2
df_pivoted['Mean zone C'] = (df_pivoted[('C', 1)] + df_pivoted[('C', 2)]) / 2

# Reset the index to have 'date' and 'time' as separate columns
df_pivoted.reset_index(inplace=True)
df_pivoted.columns = ['date', 'Zone B subzone 1', 'Zone B subzone 2', 'Zone C subzone 1', 'Zone C subzone 2', 'Mean zone B', 'Mean zone C']

# Split 'date' column into 'date' and 'time'
df_pivoted[['date', 'time']] = df_pivoted['date'].str.split(expand=True)

# Save the result to a new CSV file
df_pivoted.to_csv('/home/cdacea/GH_data/mean_PAR_data.csv', index=False)

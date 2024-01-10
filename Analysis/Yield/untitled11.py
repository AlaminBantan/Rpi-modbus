import pandas as pd
import matplotlib.pyplot as plt

# Replace the path with your actual file path
file_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Results\Yield data zone b.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert 'Weight (g)' column to numeric (remove commas and convert to integer)
df['Weight (g)'] = df['Weight (g)'].replace(',', '', regex=True).astype(int)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by 'Treatment' and calculate cumulative weight for each treatment
df['Cumulative Weight'] = df.groupby('Treatment')['Weight (g)'].cumsum()

# Custom color palette
custom_palette = {'BC1': 'blue', 'BC2': 'lightblue', 'BM1': '#FFD700', 'BM2': 'orange'}

# Plotting the cumulative weight over time for each treatment with custom colors
plt.figure(figsize=(10, 6))
for treatment, group in df.groupby('Treatment'):
    plt.plot(group['Date'], group['Cumulative Weight'], label=treatment, color=custom_palette[treatment])
    

plt.title('Cumulative Weight Over Time in Zone B')
plt.xlabel('Date')
plt.ylabel('Cumulative Weight (g)')
plt.xticks(rotation=45)
plt.legend()
save_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Results\Zone B\cumulative_weight_zone_B.svg"
plt.savefig(save_path, format='svg')
plt.show()

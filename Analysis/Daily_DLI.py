import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file
file_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Data collection\Climatic_data\mean_PAR_data.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Exclude data for November 29th
df = df[df['date'].dt.date != pd.Timestamp('2023-11-29').date()]

# Filter out rows with missing values in Mean zone B and Mean zone C
df = df.dropna(subset=['Mean zone B', 'Mean zone C'])

# Group by date and calculate DLI for Mean Zone B and Mean Zone C
daily_dli = df.groupby('date').apply(lambda group: (group['Mean zone B'].sum() * 15 * 60 / 1000000, group['Mean zone C'].sum() * 15 * 60 / 1000000))

# Extract the results for plotting
dates = [date.date() for date, _ in daily_dli.items()]
mean_zone_b_dli_values = [mean_zone_b_dli for _, (mean_zone_b_dli, _) in daily_dli.items()]
mean_zone_c_dli_values = [mean_zone_c_dli for _, (_, mean_zone_c_dli) in daily_dli.items()]

# Plotting Mean Zone B
plt.figure(figsize=(10, 6))
plt.plot(dates, mean_zone_b_dli_values, label='Mean Zone B DLI', marker='o')
plt.xlabel('Date')
plt.ylabel('DLI (mol/m^2)')
plt.title('Daily Light Integral (DLI) for Mean Zone B')
plt.legend()
plt.xticks(rotation=45)
plt.ylim(10, 35)  # Set y-axis limits
plt.tight_layout()

# Save the plot as SVG in the specified folder
output_folder = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Data collection\Climatic_data\plots\PAR"
os.makedirs(output_folder, exist_ok=True)
output_path_b = os.path.join(output_folder, 'mean_zone_b_dli_plot.svg')
plt.savefig(output_path_b)
plt.close()

# Plotting Mean Zone C
plt.figure(figsize=(10, 6))
plt.plot(dates, mean_zone_c_dli_values, label='Mean Zone C DLI', marker='o', color='orange')
plt.xlabel('Date')
plt.ylabel('DLI (mol/m^2)')
plt.title('Daily Light Integral (DLI) for Mean Zone C')
plt.legend()
plt.xticks(rotation=45)
plt.ylim(10, 35)  # Set y-axis limits
plt.tight_layout()

# Save the plot as SVG in the specified folder
output_path_c = os.path.join(output_folder, 'mean_zone_c_dli_plot.svg')
plt.savefig(output_path_c)
plt.close()

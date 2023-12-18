# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:42:38 2023

@author: bantanam
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Data collection\Climatic_data\mean_Temperature_data.csv"
df = pd.read_csv(file_path)

# Combine date and time columns into a single datetime column
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

# Set the datetime column as the index
df.set_index('datetime', inplace=True)

# Calculate the hourly average of Mean Zone B and Mean Zone C
hourly_average_B = df.groupby(df.index.hour).agg({'Mean zone B': 'mean'})
hourly_average_C = df.groupby(df.index.hour).agg({'Mean zone C': 'mean'})

# Plot the hourly averages for Mean Zone B
plt.figure(figsize=(10, 6))
hourly_average_B.plot(marker='o', linestyle='-', color='blue')
plt.title('Hourly Average of Mean Zone B (Temperature)')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Value')
plt.grid(True)

# Save the plot in the specified directory
plt.savefig(r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Data collection\Climatic_data\plots\Temp\Hourly_Average_Mean_Zone_B_Temperature.png")

# Show the plot
plt.show()

# Plot the hourly averages for Mean Zone C
plt.figure(figsize=(10, 6))
hourly_average_C.plot(marker='o', linestyle='-', color='green')
plt.title('Hourly Average of Mean Zone C (Temperature)')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Value')
plt.grid(True)

# Save the plot in the specified directory
plt.savefig(r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Data collection\Climatic_data\plots\Temp\Hourly_Average_Mean_Zone_C_Temperature.png")

# Show the plot
plt.show()

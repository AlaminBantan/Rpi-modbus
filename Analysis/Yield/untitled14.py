# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:52:44 2024

@author: bantanam
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Replace the path with the actual path to your CSV file
csv_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Results\Yield data zone b.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Convert the 'Date' column to datetime format for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Extract only the date part from the 'Date' column
df['Date'] = df['Date'].dt.date

# Order of treatments
treatments_order = ['BC1', 'BM1', 'BM2', 'BC2']

# Group data by 'Treatment' and 'Date' and calculate the mean of 'Average fruit (g/fruit)' for each group
grouped_data = df.groupby(['Treatment', 'Date'])['Average fruit (g/fruit)'].mean().reset_index()

# Create a dictionary to map treatments to numeric values for better positioning on the x-axis
treatment_mapping = {treatment: idx for idx, treatment in enumerate(treatments_order)}

# Custom color palette
custom_palette = {'BC1': 'blue', 'BC2': 'lightblue', 'BM1': '#FFD700', 'BM2': 'orange'}

# Plotting
plt.figure(figsize=(12, 8))

bar_width = 0.2  # Width of each bar
bar_positions = np.arange(len(df['Date'].unique()))  # X-axis positions for each time point

# Create a grouped bar chart for each treatment with custom colors and specified order
for i, treatment in enumerate(treatments_order):
    treatment_data = grouped_data[grouped_data['Treatment'] == treatment]
    plt.bar(
        bar_positions + i * bar_width,
        treatment_data['Average fruit (g/fruit)'],
        width=bar_width,
        label=treatment,
        alpha=0.7,
        color=custom_palette[treatment]
    )

plt.title('Average Fruit (g/fruit) Over Time in zone B')
plt.xlabel('Date')
plt.ylabel('Average Fruit (g/fruit)')
plt.xticks(bar_positions + bar_width * (len(treatments_order) - 1) / 2, df['Date'].unique(), rotation=45, ha='right')
plt.legend()

# Save the figure as an SVG file
save_path = r"C:\Users\bantanam\KAUST\CDA-CEA Team - Documents\CO2 misting - Cucumber trial\Results\Zone B\average_fruit_bar_chart.svg"
plt.savefig(save_path, format='svg')

plt.show()

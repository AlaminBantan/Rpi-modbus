import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is stored in a CSV file named 'your_data.csv'
# If it's stored in a different format, you can adjust the read function accordingly.
df = pd.read_csv('/home/cdacea/GH_data/modified_data_15min.csv')

# Filter data for each zone and subzone combination
zone_b_subzone_1 = df[(df['Zone'] == 'B') & (df['Subzone'] == 1)]
zone_b_subzone_2 = df[(df['Zone'] == 'B') & (df['Subzone'] == 2)]
zone_c_subzone_1 = df[(df['Zone'] == 'C') & (df['Subzone'] == 1)]
zone_c_subzone_2 = df[(df['Zone'] == 'C') & (df['Subzone'] == 2)]

# Plotting the graphs
plt.figure(figsize=(12, 8))

# Plot for 'CO2 conc'
plt.plot(zone_b_subzone_1['RoundedDateTime'], zone_b_subzone_1['CO2 conc'], label='Zone B Subzone 1 CO2 Conc')
plt.plot(zone_c_subzone_1['RoundedDateTime'], zone_c_subzone_1['CO2 conc'], label='Zone C Subzone 1 CO2 Conc')

plt.xticks(rotation='vertical')
# Add labels and legend
plt.xlabel('Time')
plt.ylabel('CO2 Concentration')
plt.title('CO2 Concentration for Different Zones and Subzones')
plt.legend()

# Save the plot as an SVG file
plt.savefig('co2_concentration_plot.svg')

# Show the plot
plt.show()

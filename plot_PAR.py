import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter

# Assuming your data is stored in a CSV file named 'your_data.csv'
# If it's stored in a different format, you can adjust the read function accordingly.
df = pd.read_csv('/home/cdacea/GH_data/modified_data_15min.csv')

# Filter data for each zone and subzone combination
zone_b_subzone_1 = df[(df['Zone'] == 'B') & (df['Subzone'] == 1)]
zone_b_subzone_2 = df[(df['Zone'] == 'B') & (df['Subzone'] == 2)]
zone_c_subzone_1 = df[(df['Zone'] == 'C') & (df['Subzone'] == 1)]
zone_c_subzone_2 = df[(df['Zone'] == 'C') & (df['Subzone'] == 2)]

# Plotting the graphs
plt.figure(figsize=(20, 20))

# Plot for 'PAR'
plt.plot(zone_b_subzone_1['RoundedDateTime'], zone_b_subzone_1['PAR'], label='Zone B Subzone 1 PAR')
plt.plot(zone_b_subzone_2['RoundedDateTime'], zone_b_subzone_2['PAR'], label='Zone B Subzone 2 PAR')
plt.plot(zone_c_subzone_1['RoundedDateTime'], zone_c_subzone_1['PAR'], label='Zone C Subzone 1 PAR')
plt.plot(zone_c_subzone_2['RoundedDateTime'], zone_c_subzone_2['PAR'], label='Zone C Subzone 2 PAR')

# Set the x-axis ticks to show time only with one tick per hour
plt.gca().xaxis.set_major_locator(HourLocator(interval=1))
plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M"))

# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('PAR (umol.m-2.s-1)')
plt.title('PAR for Different Zones and Subzones')
plt.legend()

# Show the plot
plt.savefig('par_plot.svg')
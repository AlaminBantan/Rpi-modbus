import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/cdacea/GH_data/mean_PAR_data.csv', parse_dates=['time'])

# Plotting
plt.figure(figsize=(12, 6))

# Plotting for each zone (you can customize this based on your requirement)
for zone in ['Zone B subzone 1', 'Zone B subzone 2', 'Zone C subzone 1', 'Zone C subzone 2']:
    plt.plot(df['time'], df[zone], label=zone)

# Plotting mean values
plt.plot(df['time'], df['Mean zone B'], label='Mean zone B', linestyle='--', linewidth=2, color='black')
plt.plot(df['time'], df['Mean zone C'], label='Mean zone C', linestyle='--', linewidth=2, color='gray')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('PAR')
plt.title('PAR Data over Time')
plt.legend()
plt.grid(True)

# Save the plot as an SVG file
plt.savefig('/home/cdacea/GH_data/plots/par_plot.svg')

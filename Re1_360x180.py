import xarray as xr
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# File path
file_path = r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap360x180.nc"

# Open the dataset
data = xr.open_dataset(file_path)

# Extract the 'ha' variable
ha_data = data['ha'].isel(nc=0)

# Adjust longitude coordinates to be in the range of 0 to 360 degrees
ha_data['lon'] = (ha_data['lon'] + 360) % 360

# Sort the data by longitude
sorted_ha_data = ha_data.sortby('lon')

# Roll the data to shift longitudes
# Find the index where longitude is close to 200
roll_index = sorted_ha_data['lon'].values.searchsorted(200)
shifted_ha_data = sorted_ha_data.roll(lon=roll_index, roll_coords=True)

# Convert to a 2D array for heatmap plotting
data_array = shifted_ha_data.values

# Create latitude and longitude labels for the heatmap
lat_labels = shifted_ha_data['lat'].values
lon_labels = shifted_ha_data['lon'].values

# Plot the heatmap using Seaborn
plt.figure(figsize=(12, 6))
sns.heatmap(data_array, cmap='viridis', vmin=0, vmax=0.5, xticklabels=lon_labels, yticklabels=lat_labels)
plt.title('Shifted Tidal Elevation Data')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

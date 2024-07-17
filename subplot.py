

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

# File paths
file_paths = [
    r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap3600x1800.nc",
    r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap720x360.nc",
    r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap360x180.nc"
]

# Plot titles for each subplot
plot_titles = ['3600x1800', '720x360', '360x180']

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
print("hemant")
for i, file_path in enumerate(file_paths):
    # Open the NetCDF file
    dataset = nc.Dataset(file_path)
    
    # Select the first time slice where data is 3D (time, lat, lon)
    hp = dataset.variables['hp'][0, :, :]
     
    ha = dataset.variables['ha'][0, :, :] 
    
    # Get the coordinates (assuming variables are named 'lon' for longitude and 'lat' for latitude)
    lon = dataset.variables['lon'][:]
    lat = dataset.variables['lat'][:]
    #print("hemant")
    # Create the contour plot
    ax = axes[i]
    print(i)
    if(i==2):
        contour_amplitude = ax.imshow(ha,
        aspect='auto',
        vmin=0,
        vmax=0.5,
        extent=(0,360, -90, 90),
        origin="lower")
    else:
        contour_amplitude = ax.imshow(ha,
        aspect='auto',
        vmin=0,
        vmax=0.5,
        extent=(-180,180, -90, 90),
        origin="lower")
   # ax.colorbar(contour_amplitude, label='Amplitude (ha)')
    #contour = ax.contourf(lon, lat, hp, cmap='viridis', levels=50)
#    if(i==2):
#        ax.contour(lon, lat, hp, colors='black', levels=5)
#    else:
    ax.contour(lon, lat, hp, colors='black', levels=5)
    ax.set_title(plot_titles[i])
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    # Add colorbar
    fig.colorbar(contour_amplitude, ax=ax, orientation='vertical')

# Adjust layout
plt.tight_layout()
plt.show()


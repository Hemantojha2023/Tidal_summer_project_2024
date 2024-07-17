


import xarray as xr

file_path = r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap720x360.nc"

# Open the NetCDF file using xarray
data = xr.open_dataset(file_path)

# Print the dataset to understand its structure and identify the relevant variable
print(data)

# compute the mean for 'ha' variable which  contain tidal elevation data
mean_elevation = data['ha'].mean().item()

# Print the mean elevation
print(f"Mean tidal elevation: {mean_elevation} meters")

# Close the dataset
data.close()


# Mean tidal elevation: 0.03687932263425249 meters
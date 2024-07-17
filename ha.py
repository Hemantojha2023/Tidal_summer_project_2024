



import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Define the path to your NetCDF file
file_path = r"C:\Users\Hemant Ojha\summer_project_2024\h_tpxo9_remap3600x1800.nc"

# Open the NetCDF file using xarray
data = xr.open_dataset(file_path)

# Create a figure
fig = plt.figure(figsize=(20, 12))

# Create a GridSpec with extra space for the color bar
gs = GridSpec(3, 6, width_ratios=[1, 1, 1, 1, 1, 0.05], wspace=0.4, hspace=0.4)

# Loop through nc=0 to nc=14
for nc_index in range(15):  # This loop goes from nc=0 to nc=14
    # Access the 'ha' variable for each nc index
    ha_variable = data['ha'][nc_index, :, :]

    # Determine subplot position
    row_index = nc_index // 5  # Determine row index
    col_index = nc_index % 5   # Determine column index

    # Create an axis in the grid
    ax = fig.add_subplot(gs[row_index, col_index])

    # Plot the 'ha' variable using imshow
    im = ax.imshow(
        ha_variable,
        aspect='auto',
        vmin=0,
        vmax=0.5,
        extent=(-180, 180, -90, 90),
        origin="lower"
    )
    ax.set_title(f'nc={nc_index}')
    ax.set_xlabel('Longitude [degrees_east]')
    ax.set_ylabel('Latitude [degrees_north]')

    # Add a color bar to the right of the fifth column
    cbar_ax = fig.add_subplot(gs[:, -1])
    cbar = fig.colorbar(im, cax=cbar_ax, orientation='vertical')
    cbar.set_label('Tidal Elevation Amplitude at Z nodes [meter]')
    plt.savefig('test_ha.pdf')
    # Show plot
#plt.show()

# Close the dataset
data.close()






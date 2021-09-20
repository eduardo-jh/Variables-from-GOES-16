# -*- coding: utf-8 -*-
"""
ATMO555 Assignment E3. Plotting variables from GOES16

Created on Sun Sep 19 10:51:21 2021

@author: eduardo
"""

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import cartopy.crs as ccrs
 

def plot_variable(lon, lat, variable, varname):
    """ A function that plots one variable at the time """

    # Create a figure
    plt.figure(figsize=(12,12))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    
    # Plot data
    plt.pcolor(lon, lat, variable, transform=ccrs.PlateCarree(), cmap='RdYlBu_r')
    plt.title(varname)
    plt.colorbar(orientation="horizontal", pad=0.06)#fraction=0.05)
    
    # Extent from metadata: ULC: 060.00 -120.00 LRC: 000.00 -030.00  RES:1.00 1.0
    ax.set_xticks([-120,-60,-30])
    ax.set_yticks([60,30,0])
    
    plt.savefig('snapshot_' + varname + '.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()


if __name__ == '__main__':

    # Path to the GOES 16 image file
    filename = 'D:/Downloads/CER_GEO_Ed4_GOE16_NH_V01.2_2021.181.2330.06K.nc'
    
    # Open the file using the NetCDF4 library
    nc = Dataset(filename)
    
    lat = nc.variables['latitude'][:]
    lon = nc.variables['longitude'][:]
    
    # Generate plots from a list of variables
    variables = ['temperature_sir', 'temperature_67', 'temperature_ir',
                 'temperature_sw', 'cloud_top_height', 'cloud_bottom_height',
                 'cloud_effective_height']
    
    for var in variables:
        print('Generating plot for {0}... please wait.'.format(var))
        # Extract the variables from the NetCDF
        data = nc.variables[var][:]
        plot_variable(lon, lat, data, var)
    
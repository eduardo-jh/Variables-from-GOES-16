# -*- coding: utf-8 -*-
"""
ATMO555 Assignment E3. Plotting Solar Zenith Angle from GOES16
Created on Wed Sep 15 11:37:55 2021

@author: eduardo
"""
from osgeo import gdal
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

THRESHOLD = 200 # Remove data below this value
MAX = 310
MIN = 200

# Open the netCDF4 file
dr = 'D:/Downloads/ATMO555/Assignment_E3/'
fn = 'CER_GEO_Ed4_GOE16_NH_V01.2_2021.181.2330.06K.nc'

# Open the file
ds = gdal.Open(dr+fn, gdal.GA_ReadOnly)

datasets = ds.GetSubDatasets()

# Print the datasets to see their names and select the one you want
for i, db in enumerate(datasets):
    print(i, db[0])

# The first dataset is 'solar_zenith_angle'
band = gdal.Open(datasets[0][0], gdal.GA_ReadOnly)

# Show metadata from the selected dataset
for key, value in band.GetMetadata().items():
    print("{:35}: {}".format(key, value))

# Get the geotransform metadata (extension) of the figure to scale the figure
geoTransform = band.GetGeoTransform()
# print(geoTransform)
minx = geoTransform[0]
maxy = geoTransform[3]
maxx = minx + geoTransform[1] * band.RasterXSize
miny = maxy + geoTransform[5] * band.RasterYSize
print("Spatial extent [minx,miny,maxx,maxy]: ", [minx, miny, maxx, maxy])

# Extract the temperature matrix data
data = band.ReadAsArray()

# Create a figure
plt.figure(figsize=(12,12))
# Extent: (left, right, bottom, top)
plt.imshow(data, extent=[minx,maxx,miny,maxy], cmap='RdYlBu_r') # This has two times: 0 or 1
plt.title('solar_zenith_angle')
plt.colorbar(orientation='horizontal', pad=0.08)
plt.savefig('snapshot_solar_zenith_angle.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

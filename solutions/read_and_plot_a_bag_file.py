import sys
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from osgeo import gdal
from osgeo import osr

# open the BAG file
bag_path = os.path.join(os.path.dirname(__file__), os.pardir, "data", "sh2007.bag")
dataset = gdal.Open(bag_path, gdal.GA_ReadOnly)
if not dataset:
    raise RuntimeError("Issue in opening the BAG file: %s" % bag_path)

# retrieve geospatial information
projection = dataset.GetProjection()
srs = osr.SpatialReference(wkt=projection)
projection_name = srs.GetAttrValue('projcs')
gt = dataset.GetGeoTransform()
if not gt:
    raise RuntimeError("Issue in retrieving the geotransfrom")

# retrieve elevation
elev_band = dataset.GetRasterBand(1)
elev_nodata = elev_band.GetNoDataValue()
elev = elev_band.ReadAsArray()
elev[elev == elev_nodata] = np.nan
elev = -elev
bag_extent = [gt[0], gt[0] + elev.shape[1] * gt[1], gt[3] + elev.shape[0] * gt[5], gt[3]]

# plot elevation
plt.figure(figsize=(15, 10))  # to make the plot bigger
ax = plt.axes()
plt.ticklabel_format(useOffset=False)  # to avoid the display of an offset for the labels
ax.xaxis.set_major_locator(ticker.MultipleLocator(100.0))  # to set the distance between labels (x axis)
ax.yaxis.set_major_locator(ticker.MultipleLocator(100.0))  # to set the distance between labels (y axis)
img = ax.imshow(elev, origin='upper', extent=bag_extent, cmap='viridis_r')  # display the array using the passed extent
ax.set_aspect('equal')  # avoid deformations for the displayed data
title = "%s\nProjection: %s" % (os.path.basename(bag_path), projection_name)
plt.title(title)  # put the filename and the projection as part of the title
plt.xlabel("Easting")
plt.ylabel("Northing")
cb = plt.colorbar(img)  # pass the 'img' object used to create the colorbar
cb.set_label('Bathymetry [meter]')
plt.grid()
plt.show()

# retrieve uncertainty
unc_band = dataset.GetRasterBand(2)
unc_nodata = elev_band.GetNoDataValue()
unc = unc_band.ReadAsArray()
unc[unc == unc_nodata] = np.nan
bag_extent = [gt[0], gt[0] + unc.shape[1] * gt[1], gt[3] + unc.shape[0] * gt[5], gt[3]]

# plot uncertainty
plt.figure(figsize=(15, 10))
ax = plt.axes()
plt.ticklabel_format(useOffset=False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(100.0))
ax.yaxis.set_major_locator(ticker.MultipleLocator(100.0))
img = ax.imshow(unc, origin='upper', extent=bag_extent)
ax.set_aspect('equal')
title = "%s\nProjection: %s" % (os.path.basename(bag_path), projection_name)
plt.title(title)  # put the filename and the projection as part of the title
plt.xlabel("Easting")
plt.ylabel("Northing")
cb = plt.colorbar(img)
cb.set_label('Uncertainty [meter]')
plt.grid()
plt.show()

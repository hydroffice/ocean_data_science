from PySide2 import QtWidgets
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

plt.figure()
projection = ccrs.Orthographic(central_longitude=-65.0, central_latitude=40.0)
ax = plt.axes(projection=projection)
ax.coastlines(color='gray', alpha=0.4)
gl = ax.gridlines(color='black', alpha=0.6, linestyle='--', xlocs=range(-180, 181, 15))
gl.xlabels_top = False
ax.stock_img()
ax.set_extent([-120, -5, 30, 150])
plt.show()

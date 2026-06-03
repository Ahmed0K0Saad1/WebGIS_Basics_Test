import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("data/gadm41_EGY_1.shp")

gdf.plot()
plt.show()

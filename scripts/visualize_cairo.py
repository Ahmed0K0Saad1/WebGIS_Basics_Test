import geopandas as gpd
import matplotlib.pyplot as plt
import os
gdf = gpd.read_file("data/gadm41_EGY_1.shp")

fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(edgecolor="black", facecolor="lightblue", ax=ax)

selected_gov = 'Al Qahirah'
gdf[gdf['NAME_1'] == selected_gov].plot(edgecolor="red", facecolor="yellow", ax=ax)
plt.show()

fig.savefig(os.path.join("output", "cairo_map.png"), dpi=300)
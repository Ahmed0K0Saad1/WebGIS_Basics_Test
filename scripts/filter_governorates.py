import geopandas as gpd
import matplotlib.pyplot as plt
import os

gdf = gpd.read_file("data/gadm41_EGY_1.shp")
print(gdf['NAME_1'].unique())

# filter the governorates you want to keep
selected_govs = gdf[gdf['NAME_1'].isin(['Al Qahirah', 'Al Jizah'])] 

# Drawing a map of the entire country of Egypt 
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(edgecolor="black", facecolor="lightblue", ax=ax)

# Drawing the selected governorates on top of the map
selected_govs.plot(edgecolor="red",facecolor="green" ,ax=ax)

# Adding labels to the selected governorates
ax.set_title("Selected Governorates in Egypt")
plt.show()

# Save output instead of showing
fig.savefig(os.path.join("output", "selected_governorates.png"), dpi=300)
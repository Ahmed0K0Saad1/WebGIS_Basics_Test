import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import os
import matplotlib.patches as mpatches

# 1: Read the shapefile containing the boundaries of Egypt's governorates
gdf = gpd.read_file("data/gadm41_EGY_1.shp")

# 2: create a polygon that represents the area of interest (e.g., a specific region in Egypt)
poly = Polygon([(28.0, 28.0), (34.0, 28.0), (34.0, 34.0), (28.0, 34.0)])  

# 3: filter the governorates that intersect with the polygon
filtered_gdf = gdf[gdf.intersects(poly)]
print("filtered_gdf:", len(filtered_gdf))
print(filtered_gdf["NAME_1"].unique())

# 4: calculate the percentage of overlap between each governorate and the polygon, and filter based on a threshold
threshold = 0.7 
filtered_govs = []
for idx, row in gdf.iterrows():
    overlap_area = row.geometry.intersection(poly).area
    total_area = row.geometry.area
    overlap_percentage = overlap_area / total_area
    if overlap_percentage >= threshold:
        filtered_govs.append(row['NAME_1'])


# 5: visualize the filtered governorates on a map
fig, ax = plt.subplots(figsize=(10, 10))

# 6: plot the original governorates
gdf.plot(ax=ax, edgecolor="black", color="whitesmoke", linewidth=0.5)

# 7: plot the polygon in red
poly_gdf = gpd.GeoDataFrame(geometry=[poly], crs=gdf.crs)
poly_gdf.plot(ax=ax, edgecolor="darkred", color="red", alpha=0.25)

# 8: plot the filtered governorates in green
filtered_final = gdf[gdf['NAME_1'].isin(filtered_govs)]
filtered_final.plot(ax=ax, edgecolor="black", color="mediumseagreen", alpha=0.7)

# 9: add labels to the filtered governorates 
for idx, row in gdf.iterrows():
    plt.text(row.geometry.centroid.x, row.geometry.centroid.y,
             row["NAME_1"], fontsize=6, ha="center", color="darkblue",
             bbox=dict(facecolor="white", alpha=0.5, edgecolor="none"))

# 10: add grid to the map
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

# 11: add labels and title
plt.title("Spatial Filtering of Governorates (Threshold = 70%)", fontsize=16, fontweight="bold")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# 11: Legend - create custom legend patches
legend_patches = [
    mpatches.Patch(color="whitesmoke", label="All Governorates"),
    mpatches.Patch(color="mediumseagreen", alpha=0.7, label="Filtered Governorates"),
    mpatches.Patch(color="red", alpha=0.25, label="Polygon Area")
]
plt.legend(handles=legend_patches, loc="upper right", title="Map Layers")

#12: save the figure 
fig.savefig(os.path.join("output", "Spatial Filtering of Governorates.png"), dpi=300)
plt.show()
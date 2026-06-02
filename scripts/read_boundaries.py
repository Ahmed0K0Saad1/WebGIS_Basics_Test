import geopandas as gdp

gdf = gdp.read_file("data/gadm41_EGY_1.shp")
print(gdf.head())

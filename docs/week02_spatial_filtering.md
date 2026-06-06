Spatial Filtering of Governorates
Objective
The aim of this task was to filter Egyptian governorates based on a polygon area of interest and a spatial overlap threshold (≥ 70%). This exercise combined geospatial analysis with visualization to validate the filtering logic.

What We Learned
Polygon Size Matters

A small polygon produced intersections without meaningful area.

Enlarging the polygon allowed us to capture significant overlaps with governorates.

Overlap Calculation

We computed the intersection area between each governorate and the polygon.

Dividing by the governorate’s total area gave us the overlap percentage.

Applying a threshold (70%) filtered only those governorates substantially covered by the polygon.

Visualization as Validation

Printing governorate names was useful, but the map gave visual confirmation.

Using colors (gray for all, green for filtered, red for polygon) made the results clear.

Adding labels, a grid, and a legend turned the map into a professional presentation.

How We Applied It
Data Handling: Read shapefiles with GeoPandas.

Geometry Operations: Used Shapely for intersections and area calculations.

Filtering Logic: Applied a threshold to select governorates.

Visualization:

Base layer: all governorates in light gray.

Polygon: red transparent overlay.

Filtered governorates: green highlight.

Labels: governorate names placed at centroids.

Legend: explained map layers.

Grid + title: improved readability.

Results
Intersecting Governorates: 21

Filtered Governorates (≥ 70% overlap): 16

Final Map: Saved as output/Spatial_Filtering_of_Governorates.png

Key Takeaway
Spatial filtering requires careful consideration of polygon size and coordinate reference systems (CRS). Visualization is not just for presentation—it is a validation tool that confirms the correctness of geospatial analysis.
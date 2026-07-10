WebGIS Basics — Egypt Spatial Analysis

Learning project | Python · GeoPandas · Clean Architecture · Real-world spatial data

🗺️ Output Preview

Spatial filtering of Egypt's administrative boundaries using GeoPandas — governorates highlighted based on attribute queries.

📌 Overview

This project is part of my structured learning journey in Geographic Information Systems and backend development.It focuses on building a professional foundation in WebGIS using Python and real-world Egyptian spatial data.

🚀 Recent Engineering Upgrades:

Applied Clean Architecture: Centralized all paths in config/settings.py.
Built a Data Catalog to manage spatial layers dynamically.
Added Deep Data Validation to check Shapefile integrity before processing.
What I practiced here:

Reading and parsing Shapefiles with GeoPandas
Filtering geographic features by attribute (governorate name, region)
Visualizing spatial data with styled choropleth maps
Structuring a scalable GIS project for portfolio use
🛠️ Tech Stack

Tool	Purpose
Python 3	Core scripting language
GeoPandas	Spatial data reading & analysis
Shapely	Geometry operations
Matplotlib	Map visualization
Git & GitHub	Version control
🗂️ Project Structure

WebGIS_Basics_Test/
│ 
├── config/ # ⚙️ System settings & Data Catalog
│
└── settings.py # Single source of truth for all paths 
│
├── data/
│ └── raw/ # Egypt administrative boundary shapefiles 
│ 
├── scripts/ # 🐍 Python analysis & validation scripts 
│ 
└── check_data.py # Verifies Shapefile integrity (.shp, .dbf, etc.) 
│ 
├── output/ # Generated maps & results 
├── docs/ 
# Setup notes & documentation 
└── README.md

text


---

## 🚀 Roadmap
- [x] Read Egypt shapefile and display all governorates
- [x] Filter and highlight specific governorates spatially
- [x] Style map output (colors, borders, titles)
- [x] Setup Clean Architecture (Centralized Settings)
- [x] Implement Deep Data Validation pipeline
- [ ] Integrate OSM road network data
- [ ] Spatial analysis: road length per governorate
- [ ] Web visualization with Leaflet.js / Mapbox GL
- [ ] Connect to PostGIS database backend

---

## 👤 About
**Ahmed Khaled Saad** — Junior GIS Developer
📍 Tanta, Egypt | GIS Student, Tanta University (Class of 2027)
🔗 [LinkedIn](https://linkedin.com/) · [GitHub](https://github.com/Ahmed0K0Saad1)

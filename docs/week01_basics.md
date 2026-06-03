#Week 1 - Basics

## ✅ Achievements
- Read Egypt administrative boundaries using GeoPandas (`gadm41_EGY_1.shp`).
- Visualized the full map of Egypt with colors and borders.
- Filtered one governorate (Cairo) and highlighted it.
- Filtered multiple governorates (Cairo and Giza) using: 
- `query` with OR. 
- `isin()` for cleaner and scalable code.
- Added a map title for clarity.
- Saved output maps into `outputs/` folder using `fig.savefig()`.

## ⚙️ Engineering Notes
- `isin()` is more efficient and readable than multiple OR conditions.
- Governorate names must match exactly (English or Arabic).
- Using `ax` allows layered plotting (all Egypt + selected governorates).
- `fig.savefig()` with `os.path.join` is more portable across operating systems.
- Always close figures (`plt.close()`) when generating multiple outputs.

## 📊 Outputs
- `output/selected_governorates.png`: Cairo and Giza highlighted in green.


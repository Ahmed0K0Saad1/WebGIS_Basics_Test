from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA = DATA_DIR / "raw"
OUTPUT_DIR = BASE_DIR / "output"
DOCS_DIR = BASE_DIR / "docs"
SCRIPTS_DIR = BASE_DIR / "scripts"

class DataCatalog:
    EGYPT_COUNTRY = RAW_DATA / "gadm41_EGY_0.shp"
    EGYPT_GOVERNORATES = RAW_DATA / "gadm41_EGY_1.shp"
    EGYPT_DISTRICTS = RAW_DATA / "gadm41_EGY_2.shp"


DEFAULT_CRS = "EPSG:4326"

def ensure_directories_exist():
    
    required_dirs = [DATA_DIR, RAW_DATA,OUTPUT_DIR,DOCS_DIR,SCRIPTS_DIR]

    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("All Required Directories Are Checked And Ready")

    if __name__ == "__main__":
        ensure_directories_exist()
        print(f"Base Directory is: {BASE_DIR}")
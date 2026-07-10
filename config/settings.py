from pathlib import Path

# 1: Base Directories
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
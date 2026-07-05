from pathlib import path

BASE_DIR = path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "raw"
MAPS_DIR = BASE_DIR / "outbut"

EGYPT_GOVERNORATES = DATA_DIR / "boundaries" / "gadm41_EGY_1.shp"

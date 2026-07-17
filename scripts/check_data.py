import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.append(str(PROJECT_ROOT))


from config.settings import DataCatalog, ensure_directories_exist

def validate_shipfile(shp_path: Path):

    print(f"\n Checking: {shp_path.name}")

    dbf_path = shp_path.with_suffix(".dbf")
    shx_path = shp_path.with_suffix(".shx")

    required_files = [shp_path,dbf_path,shx_path]

    for file_path in required_files:
        if not file_path.exists():
            print(f"ERROR: Missing File '{file_path.name}' in '{file_path.parent}'")
            print("Operation Aborted Due To Missing Spatial Data Dependencies.")
            sys.exit(1)

    print(f"SUCCESS: All Necessary Files For '{shp_path.name}' Are present.")   

if __name__ == "__main__":
    ensure_directories_exist()

    print("--- Starting Spatial Data Validation ---")

    validate_shipfile(DataCatalog.EGYPT_COUNTRY)
    validate_shipfile(DataCatalog.EGYPT_GOVERNORATES)
    validate_shipfile(DataCatalog.EGYPT_DISTRICTS)

    print(f"\n All Spatial Data Validated Successfully! Ready For Geopandas Processing")

import math
import os

from datetime import datetime
from dotenv import load_dotenv
from fhir_transformer.eclaim.file_extractor import open_dbf_files, save_json_files, json_dump
from fhir_transformer.eclaim.bundle_package import create_bundle_resource_eclaim

load_dotenv()

def process(path_2_files: str, import_time: datetime, set_no: int, slash: str):
    # Import Environment Variable
    local_output_path = os.getenv('LOCAL_OUTPUT_PATH')
    hos_addr = os.getenv('HOS_ADDR')
    hos_name = os.getenv('HOS_NAME')
    os_vm = os.getenv('OS')
    # Open Eclaim Files
    eclaim_16_df,eclaim_16_name = open_dbf_files(path_2_files, slash)
    # Prepare Bundle Resource From DBF
    bundle_resource = create_bundle_resource_eclaim(eclaim_16_df,eclaim_16_name,hos_addr,hos_name,os_vm)
    bundle_resource = json_dump(bundle_resource)
    save_json_files(local_output_path,bundle_resource)
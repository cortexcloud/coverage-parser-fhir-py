import platform
import glob
import pandas as pd
from datetime import datetime
from fhir_transformer.eclaim.processor import process

def run():
    slash = "\\" if platform.system() == "Windows" else "/"
    print(f"Converting eclaim Files in {slash}uploads{slash}eclaim{slash}")
    files = glob.glob(f".{slash}uploads{slash}eclaim{slash}*")
    if len(files) == 0:
        print(f"No file found in .{slash}uploads{slash}eclaim{slash}")
    else:
        print(f"{len(files)} file found in .{slash}uploads{slash}eclaim{slash}")
        print(f"Try matching the files")

        eclaim_path_files = list()

        for file in files:
            eclaim_path_files.append(file)
        process(eclaim_path_files,datetime.now().date(),1,slash)
run()
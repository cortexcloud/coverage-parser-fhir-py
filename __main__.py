import platform
import glob
import pandas as pd
from datetime import datetime
from fhir_transformer.eclaim.processor import process

def run():
    slash = "\\" if platform.system() == "Windows" else "/"
    print(f"Converting eclaim Files in {slash}uploads{slash}eclaim{slash}")
    files_dbf = glob.glob(f".{slash}uploads{slash}eclaim{slash}dbf{slash}*")
    if len(files_dbf) == 0:
        files_csv = glob.glob(f".{slash}uploads{slash}eclaim{slash}txt{slash}*")
        if len(files_csv) == 0:
            print(f"No file found in .{slash}uploads{slash}eclaim{slash}")
        else:
            print(f"{len(files_csv)} file found in .{slash}uploads{slash}eclaim{slash}txt")
            print(f"Try matching the files") 

            eclaim_path_files = list()

            for file in files_csv:
                eclaim_path_files.append(file)
            process(eclaim_path_files,'txt',datetime.now().date(),1,slash)
    else:
        print(f"{len(files_dbf)} file found in .{slash}uploads{slash}eclaim{slash}dbf{slash}")
        print(f"Try matching the files")

        eclaim_path_files = list()

        for file in files_dbf:
            eclaim_path_files.append(file)
        process(eclaim_path_files,'dbf',datetime.now().date(),1,slash)
run()
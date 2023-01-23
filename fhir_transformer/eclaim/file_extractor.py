import encodings
import xmltodict
import sys
import re
import pandas as pd
import json
from dbfread import DBF

def open_dbf_files(file_path: str, slash: str):
    eclaim_16_df = []
    eclaim_16_name = []
    for i in file_path:
        file_name = i.split(slash)[3][:3]
        dbf = DBF(i)
        frame_dbf = pd.DataFrame(iter(dbf))
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append(file_name) 
    if 'ODX' not in eclaim_16_name:
        print(f'ODX file is not found')
        print(f'Mocking {i} file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('ODX')  
    elif 'IOP' not in eclaim_16_name:
        print(f'IOP file is not found')
        print(f'Mocking {i} file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('IOP')  
    elif 'IPD' not in eclaim_16_name:
        print(f'IPD file is not found')
        print(f'Mocking IPD file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('IPD')     
    elif 'IDX' not in eclaim_16_name:
        print(f'IDX file is not found')
        print(f'Mocking IDX file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('IDX')     
    elif 'OPD' not in eclaim_16_name:
        print(f'OPD file is not found')
        print(f'Mocking OPD file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('OPD')     
    elif 'OOP' not in eclaim_16_name:
        print(f'OOP file is not found')
        print(f'Mocking OOP file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('OOP')       
    elif 'INS' not in eclaim_16_name:
        print(f'INS file is not found')
        print(f'Mocking INS file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('INS')       
    elif 'PAT' not in eclaim_16_name:
        print(f'PAT file is not found')
        print(f'Mocking PAT file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('PAT')          
    elif 'DRU' not in eclaim_16_name:
        print(f'DRU file is not found')
        print(f'Mocking DRU file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('DRU')        
    elif 'AER' not in eclaim_16_name:
        print(f'AER file is not found')
        print(f'Mocking AER file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('AER')        
    elif 'LVD' not in eclaim_16_name:
        print(f'LVD file is not found')
        print(f'Mocking LVD file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('LVD')     
    elif 'CHT' not in eclaim_16_name:
        print(f'CHT file is not found')
        print(f'Mocking CHT file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('CHT')      
    elif 'CHA' not in eclaim_16_name:
        print(f'CHA file is not found')
        print(f'Mocking CHA file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('CHA')           
    elif 'IRF' not in eclaim_16_name:
        print(f'IRF file is not found')
        print(f'Mocking IRF file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('IRF')      
    elif 'ORF' not in eclaim_16_name:
        print(f'ORF file is not found')
        print(f'Mocking ORF file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('ORF')         
    elif 'ADP' not in eclaim_16_name:
        print(f'ORF file is not found')
        print(f'Mocking ORF file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('ORF') 
    elif 'LABFU' not in eclaim_16_name:
        print(f'LABFU file is not found')
        print(f'Mocking LABFU file .. Successfully')
        frame_dbf = pd.DataFrame()
        eclaim_16_df.append(frame_dbf)
        eclaim_16_name.append('LABFU')            
    return eclaim_16_df,eclaim_16_name
def save_json_files(file_path,json_data):
    # Writing to sample.json
    with open(file_path, "w") as outfile:
        outfile.write(json_data)
    print('Saving Json Files..')
def json_dump(json_data):
    return json.dumps(json_data, indent=2, ensure_ascii=False, cls=NpEncoder)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
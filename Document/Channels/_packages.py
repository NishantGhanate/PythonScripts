import os
import csv
import json
import re

folderPath = r"H:\Github\PythonScripts\Document\Channels\Packages"
file_list = []
pattern = ".csv"
fileFormat = ".json"

def save(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        channels_csv = [r for r in reader]
        path = re.sub(pattern,fileFormat,path)
        print(path)
        with open(path, 'w') as outfile:
            json.dump(channels_csv, outfile)

for f in os.scandir(folderPath):
    # print(f.path)
    save(f.path)




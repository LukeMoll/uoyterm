#!/usr/bin/python3
import os
import yaml
import json
from datetime import date
import time

INPUT_DIR = "input"
OUTPUT_DIR = "output"
def main():
    if os.path.exists(INPUT_DIR) and os.path.isdir(INPUT_DIR):
        if os.path.exists(OUTPUT_DIR) and os.path.isdir(OUTPUT_DIR):
            print("Folder", INPUT_DIR+"/", "found.")
            input_files = [os.path.join(INPUT_DIR, fn) for fn in os.listdir(INPUT_DIR) if fn[-5:] == '.yaml']
            print(len(input_files), "files found.")
            data = parseYAML(input_files)
            for yearData in data.values():
                enrichYear(yearData)
            writeJSON(OUTPUT_DIR, data)
        else:
            print("No output folder")
    else:
        print("No input folder")

def parseYAML(input_files):
    allData = {}
    for filename in input_files:
        stream = open(filename, 'r')
        data = yaml.load(stream)
        allData[data['year']] = data
    return allData

def enrichYear(yearData):
    for term in ["spr", "sum", "aut"]:
        if term in yearData:
            yearData[term]['start_ts'] = time.mktime(yearData[term]['start'].timetuple())
            yearData[term]['end_ts']  =  time.mktime(yearData[term]['end'].timetuple())

def writeJSON(outputDir, data):
    for e in data.items():
        with open(os.path.join(outputDir, str(e[0]) + '.json'), 'w+') as file:
            file.write(json.dumps(e[1], default=str))

if __name__ == '__main__':
    main()

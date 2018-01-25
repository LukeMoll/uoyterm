#!/usr/bin/python3
import os
from yaml import load

def main():
    INPUT_DIR = "input"
    if os.path.exists(INPUT_DIR) and os.path.isdir(INPUT_DIR):
        print("Folder", INPUT_DIR+"/", "found.")
        input_files = [os.path.join(INPUT_DIR,fn) for fn in os.listdir(INPUT_DIR) if fn[-5:] == '.yaml']
        print(len(input_files), "files found.")
        parseYAML(input_files)
    else:
        print("No input folder")    

def parseYAML(input_files):
    for filename in input_files:
        stream = open(filename, 'r')
        data = load(stream)
        print(data)

if __name__ == '__main__':
    main()

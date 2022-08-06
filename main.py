import csv 
import json 
import sys

def csv_to_json(csv_file_path, json_file_path):
    data = []
      
    with open(csv_file_path, encoding='utf-8', errors='ignore') as csvf: 
        reader = csv.DictReader(csvf) 
        for row in reader: 
            data.append(row)
  
    with open(json_file_path, 'w', encoding='utf-8') as jsonf: 
        json_string = json.dumps(data, indent=4)
        jsonf.write(json_string)

csv_file_path = sys.argv[1]
json_file_path = sys.argv[2]
csv_to_json(csv_file_path, json_file_path)
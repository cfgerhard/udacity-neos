import csv
import json
from typing import List, Any

with open('./data/neos.csv', 'r') as f:
    neos = csv.DictReader(f)
    neos_data = [row for row in neos]
    print(len(neos_data))
    print(neos_data[0]['pdes'])
    print(str([item['diameter'] for item in neos_data if item['name'] == 'Apollo']).split("'")[1])



with open('./data/cad.json', 'r') as f:
    cad = json.load(f)
    datasets = cad['data']
    print(len(datasets))
    for item in datasets:
        if '2015 CL' in item[0] and '2000-Jan-01' in item[3]:
            print(item[4])
    for item in datasets:
        if '2002 PB' in item[0] and '2000-Jan-01' in item[3]:
            print(item[7])

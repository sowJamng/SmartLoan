import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'C:/Miage/ML/projet/Biblio.csv'
jsonFilePath = r'data.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")

# converting dataFrame to JSON
"""
df.to_json(
    path_or_buf='file/music.json',
    orient='split',  # other options are (split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’)
    date_format='epoch',
    double_precision = 2,
    force_ascii=False,
    date_unit='ms',
    default_handler=None,
    lines=False, # orient must be records to set this True
    #compression='zip',
    index=False, # it works only when orient is split or table
    indent=2    
)
"""
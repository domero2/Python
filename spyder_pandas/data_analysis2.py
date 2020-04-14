import numpy as np
import pandas as pd
import os
from os import path
import json

#Defined file path
BASE_PATH = path.dirname(path.abspath(__file__))
CSV_PATH = BASE_PATH + '\Art_work.csv'
NewFilePath= BASE_PATH + "\Results\Resultcsv.csv"
JSON_PATH = BASE_PATH + '\json_files'

#Lists defined
Column_to_use = ['id','artist','title','medium','year','acquisitionYear','height','width','units']
Json_records = [("Book1","$3","ZyszekAutor"),("Book2","$4","JanekAutor"), ("Book5", None, None)]
KEY_COLUMN_TO_USE = ['id','all_artists','title','medium','acquisitionYear','height','width','units']

#Generate data from part of the file
GenerateChosenColumn = pd.read_csv(CSV_PATH,nrows=5, index_col='id', usecols=Column_to_use)
#Save generated data into new file
GenerateChosenColumn.to_csv(path_or_buf=NewFilePath, sep=",", mode='w', encoding='UTF-8')

# assign to variable dataframe of json input
Jsonresults= pd.DataFrame(Json_records, columns=["BookName", "Price", "Author"])

#define own functions
def get_records_from_json(file_path, keys):
    """
    :param file_path: path to file
    :param file_name:  name of processed file
    :return: open file
    """
    with open(file_path) as source_data:
        content = json.load(source_data)
    results = []
    for item in keys:
        results.append(content[item])
    return tuple(results)

#Function will iterate through directory and get only first two json files from path
def iterate_through_json(keys):
    results = []
    for root, subfolder, final in os.walk(JSON_PATH):
        for item in final[:2]:
            if item.endswith('json'):
                recordsToAppend = get_records_from_json(path.join(root,item),
                                                        keys)
                results.append(recordsToAppend)
                
    frameData = pd.DataFrame.from_records(results,columns =keys , index='id')
    return frameData
    
Data_iterate = iterate_through_json(KEY_COLUMN_TO_USE)

readArtist = pd.read_csv(CSV_PATH) 
artistResults = readArtist['artist']

#res=pd.unique(artistResults)
#count_specyfic = readArtist['artist'] == 'Blake, Robert'
#result_count = count_specyfic.value_counts()

#Read artist name which has index number =1035
readArtist.loc[1035,'artist']

#Read value from first row and first column    
readArtist.iloc[0,0]
#read valeu for each column for first row
readArtist.iloc[0,:]

#Sorted values from beginnign and from the end
readArtist['width'].sort_values().head()
readArtist['width'].sort_values().tail()

#Modify not a nmber to number and enforce for errors for width column
pd.to_numeric(readArtist['width'],errors='coerce')
readArtist.loc[:,'width'] = pd.to_numeric(readArtist['width'],errors='coerce')

#Modify not a nmber to number and enforce for errors for height column
pd.to_numeric(readArtist['height'],errors='coerce')
readArtist.loc[:,'height'] = pd.to_numeric(readArtist['height'],errors='coerce')

#Multiply height and width
readArtist['width'] * readArtist['height']
readArtist['units'].value_counts()

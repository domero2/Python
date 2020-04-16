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

res=pd.unique(artistResults)
count_specyfic = readArtist['artist'] == 'Blake, Robert'
result_count = count_specyfic.value_counts()

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

##################################GROUPING
#Gropuing part of pandas
smallDataSet = readArtist.iloc[0:1234, :].copy()
groupedSet = smallDataSet.groupby('artist')


for name_df,group_df in groupedSet:
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name_df,min_year))
    
def fill_empty_values(series):
    value_counted = series.value_counts()
    if value_counted.empty:
        return series
    most_frequent = value_counted.index[0]
    final_set = series.fillna(most_frequent)
    return final_set
    
def transform_data(source_df):
    newOneDataFrame =[]
    for name_tf, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:,'medium'] = fill_empty_values(group_df['medium'])
        newOneDataFrame.append(filled_df)
    finallDataFrame = pd.concat(newOneDataFrame)
    return finallDataFrame
        

dataFrameFilled = transform_data(smallDataSet)

#made same using build in function
buildInFunc = smallDataSet.groupby('artist')['medium']
smallDataSet.loc[:, 'medium'] = buildInFunc.transform(fill_empty_values)

readArtist.groupby('artist')
groupedSet.min()

######################PLOTING

plotingObject = pd.read_csv(CSV_PATH, index_col='id')
#Count each year occurance in acquisitionYear column
acquisition_Year = plotingObject.groupby('acquisitionYear').size()
acquisition_Year.plot()

title_css = {'family': 'source sans pro',
             'color': 'darkblue',
             'size': '23'}
dimensionx_css = {'family': 'source sans pro',
             'color': 'darkgreen',
             'size': '19'}
dimensiony_css = {'family': 'source sans pro',
             'color': 'darkorange',
             'size': '19'}

rcParams.update({'figure.autolayout' : True, 'axes.titlepad' :20})

fig = pyplot.figure()
subplot = fig.add_subplot(1,1,1)
# rotate x values 45 degree
acquisition_Year.plot(ax=subplot, rot =45, logy=True, grid=True)
subplot.set_xlabel('Acq year', fontdict=dimensionx_css)
subplot.set_ylabel('Artworks acquired', fontdict = dimensiony_css, labelpad =10)
subplot.locator_params(nbins=35, axis='x')
subplot.set_title("Artwork year and acquisition", fontdict = title_css)

fig.show()
fig.savefig('final.png')

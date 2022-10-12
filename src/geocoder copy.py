##TO DO:

#refactor to class
#refactor so it can be more usuable with other datasets
#have the option for all of illinois
#have the option for just chicago
#

#%%
import pandas as pd
import numpy as np
import math
from helpers import *

#from riaa import *

##### Helper functions ######
#%%

    
def geoCodeChunk(numerical,direction,street_name,database_df):
    
    complete_conditional = database_df[(database_df['St_Name'] == street_name) 
                                & (database_df['St_PreDir'] == direction)
                                & (database_df['Add_Number'] < numerical + 100)
                                & (database_df['Add_Number'] >= numerical)
                                ]
    
    '''
     Improve selection criteria from the result set
    '''
    
    
    list_zipcodes = list(set(complete_conditional['Post_Code']))
    list_lat = list(set(complete_conditional['Lat']))
    list_long = list(set(complete_conditional['Long']))
    
    
    return [list_zipcodes, list_lat,list_long]



def geoCodeToDf(chunkDfName,columnNamesList):
    newDataframe = pd.DataFrame.from_records(chunkDfName, columns=[columnNamesList])
    return newDataframe

#this grabs the list of zipcodes
def extractElement(columnList):
    try:
        return columnList[0]
    except:
        return None

def extractSpecificElement(columnList,loc1,loc2):
    try:
        return columnList[loc1][loc2]
    except:
        return None

def toString(elements):
    return list(set([str(x) for x in elements]))
    
###### read in cook county address ######
address_points = pd.read_csv('../input/cook_locations.csv')

#print(address_points.head())

cook_columns = ['CMPADDABRV', 'Lat', 'Long', 'PLACENAME', 'Post_Code', 'OBJECTID','ADDRDELIV','Add_Number','St_PreDir', 'St_Name']
cook_locations = address_points[cook_columns]

#data for geocoder matches
database = cook_locations[cook_locations['PLACENAME'] =='Chicago']

#get rid of null zip code values
cook_locations_clean = cook_locations[~cook_locations['Post_Code'].isnull()]
#print(cook_locations_clean.shape)


#%%

oemc_locations = pd.read_csv('../input/oemc_locations.csv')
oemc_clean_locations = oemc_locations[~oemc_locations['numerical'].str.isupper()]


#get rid of weird outlier
oemc_clean_locations = oemc_clean_locations[oemc_clean_locations['EventNumber'] != 2011910398 ]

### Clean numerical part of oemc numerical part

#print(oemc_clean_locations.dtypes)

oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].astype(str)
oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].str.strip()
oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].astype(int)


### Clean up street names in oemc data #####

oemc_clean_locations['clean_street_name'] = oemc_clean_locations['street_name']


omec_nonS = oemc_clean_locations[~oemc_clean_locations['street_name'].str.contains("/",na=False)]
omec_s = oemc_clean_locations[oemc_clean_locations['street_name'].str.contains("/",na=False)]

#grab the beginning of the string until the forward slash /
omec_s['clean_street_name'] = omec_s['street_name'].str.replace("(?:/).*",'',regex=True)
omec_s['clean_street_name'] = omec_s['clean_street_name'].apply(helpers.splitUp)
omec_complete = pd.concat([omec_nonS,omec_s])


###### clean oemc data directional ######

#strip the any trailing white space
omec_complete['directional'] = omec_complete['directional'].str.strip()
omec_complete['directional']= omec_complete['directional'].apply(helpers.fullDirections)

###### create data chunks ######
chunkDf = np.array_split(omec_complete,30)
chunkDf[0]


######  prepare for final output ######

oemc_output = None
oemc_output = pd.DataFrame(columns=['EventNumber', 'EntryDate', 'EventType', 'TypeDescription', 'FinalDisposition', 'Location', 'CPDUnitList', 'CFDUnitList', 'numerical', 'directional', 'street_name', 'suffix' , 'zipcodes','lats','longs','clean_street_name','zipcode_list'])
test_chunk = chunkDf[0].head()


#%%

def setup(rangeNumStart,rangeNumEnd):
    df = None
    df_complete = None
    for i in range(rangeNumStart,rangeNumEnd):
        df_results = chunkDf[i].apply(lambda x: geoCodeChunk(x["numerical"],x["directional"],x["clean_street_name"],database),axis=1)
        #exec(f'df_results = chunkDf[{i}].apply(lambda x: geoCodeChunk(x["numerical"],x["directional"],x["clean_street_name"],database),axis=1)')
        df = df_results.to_frame(name='raw_results')
        codes = df['raw_results'].apply(extractSpecificElement, args =(0,0))
        df['zipcodes'] = codes
    
        lats = df['raw_results'].apply(extractSpecificElement,args =(1,0))
        df['lats'] = lats
    
        longs = df['raw_results'].apply(extractSpecificElement,args = (2,0))
        df['longs'] = longs

        ziplist = df['raw_results'].apply(extractElement)
        df['zipcode_list'] = ziplist
    
        df_complete = pd.concat([chunkDf[i], df], axis=1)
        oemc_output2 = pd.concat([oemc_output,df_complete])

        print('Done')
    return oemc_output2

#%%
#result_setup = setup(0,1)
#test chuck

#%%
result_setup = setup(0,6)
#%%
result_setup2 = setup(6,12)
result_setup3 = setup(12,18)
result_setup4 = setup(18,24)
result_setup5 = setup(24,30)

#%%
print(result_setup2)
#%%
end_result = pd.concat([result_setup,result_setup2,result_setup3,result_setup4,result_setup5])
print(len(end_result))
    

#%%
end_result.shape
end_result.head()
#%%
end_result['zipcode_list'] = end_result['zipcode_list'].apply(toString)
end_result.to_csv('oemc_output_data2.csv')
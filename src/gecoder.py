#%%
import pandas as pd
import numpy as np

##### Helper functions ######
#%%
#create function to split upt clean_street_name and then just grab the street name
def splitUp(word):
    w = word.split(' ')
    return w[0]
    
def fullDirections(direction):
    if direction == 'W':
        return 'WEST'
    if direction == 'E':
        return 'EAST'
    if direction == 'S':
        return 'SOUTH'
    if direction == 'N':
        return 'NORTH'
    else:
        return direction


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

#this grabs the first item of list of zipcodes
def extractElement1(columnList):
    try:
        return columnList[0][0]
    except:
        return None
        
#this grabs the first item of list of lats
def extractElement2(columnList):
    try:
        return columnList[1][0]
    except:
        return None


#this grabs the first item of list of longs
def extractElement3(columnList):
    try:
        return columnList[2][0]
    except:
        return None



###### read in cook county address ######
address_points = pd.read_csv('../cook_locations.csv')

#print(address_points.head())

cook_columns = ['CMPADDABRV', 'Lat', 'Long', 'PLACENAME', 'Post_Code', 'OBJECTID','ADDRDELIV','Add_Number','St_PreDir', 'St_Name']
cook_locations = address_points[cook_columns]

#data for geocoder matches
database = cook_locations[cook_locations['PLACENAME'] =='Chicago']




#print(cook_locations.head)
#print(cook_locations.shape)

#get rid of null zip code values
cook_locations_clean = cook_locations[~cook_locations['Post_Code'].isnull()]
#print(cook_locations_clean.shape)




oemc_locations = pd.read_csv('../oemc_locations.csv')
oemc_clean_locations = oemc_locations[~oemc_locations['numerical'].str.isupper()]


#get rid of weird outlier
oemc_clean_locations = oemc_clean_locations[oemc_clean_locations['EventNumber'] != 2011910398 ]


#print(oemc_locations.head())
#print(oemc_locations.shape)
#print(oemc_clean_locations.shape)

### Clean numerical part of oemc numerical part

#print(oemc_clean_locations.dtypes)

oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].astype(str)
oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].str.strip()
oemc_clean_locations['numerical'] = oemc_clean_locations['numerical'].astype(int)

#print(oemc_clean_locations.dtypes)


### Clean up street names in oemc data #####

oemc_clean_locations['clean_street_name'] = oemc_clean_locations['street_name']


omec_nonS = oemc_clean_locations[~oemc_clean_locations['street_name'].str.contains("/",na=False)]
omec_s = oemc_clean_locations[oemc_clean_locations['street_name'].str.contains("/",na=False)]

#grab the beginning of the string until the forward slash /
omec_s['clean_street_name'] = omec_s['street_name'].str.replace("(?:/).*",'',regex=True)
omec_s['clean_street_name'] = omec_s['clean_street_name'].apply(splitUp)
omec_complete = pd.concat([omec_nonS,omec_s])

 
#print(omec_nonS.shape)
#print(omec_s.shape)
#print(oemc_clean_locations.head())
#print(omec_s.head())
#print(omec_complete)

###### clean oemc data directional ######

#strip the any trailing white space
omec_complete['directional'] = omec_complete['directional'].str.strip()
omec_complete['directional']= omec_complete['directional'].apply(fullDirections)

###### create data chunks ######
chunkDf = np.array_split(omec_complete,30)
chunkDf[0]


######  prepare for final output ######

oemc_output = None
oemc_output = pd.DataFrame(columns=['EventNumber', 'EntryDate', 'EventType', 'TypeDescription', 'FinalDisposition', 'Location', 'CPDUnitList', 'CFDUnitList', 'numerical', 'directional', 'street_name', 'suffix' , 'zipcodes','lats','longs','clean_street_name','zipcode_list'])
test_chunk = chunkDf[0].head()


###TEST THE FIRST 5 ROWS of OEMC DATA ######
#list_results = test_chunk.apply(lambda x: geoCodeChunk(x["numerical"],x["directional"],x["clean_street_name"],database),axis=1)
#print(list_results)





df = None

df_complete = None

for i in range(1):
    exec(f'df_results = chunkDf[{i}].apply(lambda x: geoCodeChunk(x["numerical"],x["directional"],x["clean_street_name"],database),axis=1)')
    df = df_results.to_frame(name='raw_results')
    codes = df['raw_results'].apply(extractElement1)
    df['zipcodes'] = codes
    
    lats = df['raw_results'].apply(extractElement2)
    df['lats'] = lats
    
    longs = df['raw_results'].apply(extractElement3)
    df['longs'] = longs

    ziplist = df['raw_results'].apply(extractElement)
    df['zipcode_list'] = ziplist
    
    #df = df.drop('t', axis=1)
    

        #df_final = pd.DataFrame.from_records(df_results, columns=['zipcodes','lats','longs'])
    df_complete = pd.concat([chunkDf[i], df], axis=1)
        #df_complete['zipcode'] = df_complete['zipcodes'].apply(extractElement)
        #df_complete['lat'] = df_complete['lats'].apply(extractElement)
        #df_complete['long'] = df_complete['longs'].apply(extractElement)
    oemc_output = pd.concat([oemc_output,df_complete])

    print('Done')

#%%
print(oemc_output)

print(len(oemc_output['zipcode_list'])>1)

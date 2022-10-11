import pandas as pd

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

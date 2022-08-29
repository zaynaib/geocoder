import pandas as pd

###### read in cook county address ######
address_points = pd.read_csv('cook_locations.csv')

#print(address_points.head())

cook_locations = address_points[['Add_Number', 'ADDRDELIV','CMPADDABRV','Lat', 'Long','PLACENAME','Post_Code']]
#print(cook_locations.head)
#print(cook_locations.shape)

#get rid of null zip code values
cook_locations_clean = cook_locations[~cook_locations['Post_Code'].isnull()]
#print(cook_locations_clean.shape)



###### read in oemc data ######

oemc_locations = pd.read_csv('oemc_locations.csv')
print(oemc_locations.head())


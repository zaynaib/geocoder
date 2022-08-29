import pandas as pd
import sqlite3
import json, csv
import re
import numpy as np
import time


######
#read in cook county address
address_points = pd.read_csv('cook_locations.csv')
cook_locations = address_points[['Add_Number', 'ADDRDELIV','CMPADDABRV','Lat', 'Long','PLACENAME','Post_Code']]
cook_locations_clean = cook_locations[~cook_locations['Post_Code'].isnull()]


#read oemc locations
omec_locations = pd.read_csv('oemc_locations.csv')
omec_locations.head() 

#data cleaning convert numerical into integer so there won't be in discrepancy 
omec_clean_locations = omec_locations[~omec_locations['numerical'].str.isupper()]
omec_clean_locations = omec_clean_locations[omec_clean_locations['EventNumber'] != 2011910398 ]
omec_clean_locations['numerical'] = omec_clean_locations['numerical'].astype(str)
omec_clean_locations['numerical'] = omec_clean_locations['numerical'].str.strip()
omec_clean_locations['numerical'] = omec_clean_locations['numerical'].astype(int)


#copy original street name for clean up
omec_clean_locations['clean_street_name'] = omec_clean_locations['street_name']


omec_s = omec_clean_locations[omec_clean_locations['street_name'].str.contains("/",na=False)]
print(omec_s.head())

#clean up street names with slashes but removing everything after the slash in location
omec_s['clean_street_name'] = omec_s['street_name'].str.replace("(?:/).*",'',regex=True)


#####

###
#### HELPER FUNCTIONS

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
    






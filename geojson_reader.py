import json, csv, re
#import pandas as pd

### START CONFIGS ###
cook_geojson = 'Address_Points.geojson'
output_file = 'cook_locations.csv'
### END CONFIGS ###

#load the data
address_points = json.load(open('Address_Points.geojson'))

'''

print(address_points.keys())
print(address_points['features'][0])
print(address_points['features'][0]['properties']['CMPADDABRV'])

abbrAdd = address_points['features'][0]['properties']['CMPADDABRV']
lat = address_points['features'][0]['properties']['Long']
long = address_points['features'][0]['properties']['Lat']
post_code = address_points['features'][0]['properties']['Post_Code']


print(abbrAdd.split())

splitAdd = abbrAdd.split()
print(splitAdd[0])

'''



cleanAddress = []
address_num = []
address_direction =[]
address_street = []
address_abr = []
zipcode = []
lat = []
long = []
regAddress = []
outliers = []


headers = ['regAddress', 'cleanAddress', 'lat', 'long','zipcode']

for values in address_points['features']:
    address = values['properties']['CMPADDABRV']
    try:
        address = address.split()
        address_len = len(address)

        if address_len == 4 :
            address_num.append(address[0])
            address_direction.append(address[1])
            address_street.append(address[2])
            address_abr.append(address[3])
            cleanAddress.append(address)
            zipcode.append(values['properties']['Post_Code'])
            lat.append(values['properties']['Lat'])
            long.append(values['properties']['Long'])
            regAddress.append(values['properties']['CMPADDABRV'])
        else:
            outliers.append(address)
        
        #print(address)
        #print(outliers)

    except:
        print('something happened')




with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for i in range(len(cleanAddress)):
        content = address_num[i],address_direction[i], address_street[i], address_abr[i],zipcode[i], lat[i],long[i], regAddress[i]
        writer.writerow(content)

with open("cook_outliers.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for i in range(len(outliers)):
        writer.writerow(outliers)

        
    #first split the string
    #replace last two values with zero
    
    # address = address.replace(address[-2:], "00")
    # cleanAddress.append(address)

    #print(values['properties'])



    #print(values['properties']['CMPADDABRV'])
    #print(['properties']['CMPADDABRV'])
import json, csv, re
#import pandas as pd

### START CONFIGS ###
input_file = 'data/oemc.csv'
cook_geojson = 'Address_Points.geojson'
output_file = 'basic_geocode_locations.csv'
### END CONFIGS ###


address_points = json.load(open('Address_Points.geojson'))
#print(len(address_points['features']))

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

#re.sub(r'/\d+', '/{id}', '/andre/23/abobora/43435')

#^\d{2}(\d{2})$


#print(re.sub(r'^\d{2}(\d{2})$','00', splitAdd[0]))
'''
x = splitAdd[0].replace(splitAdd[0][2:], "00")



print(splitAdd[0][2:])
print(x)

splitAdd[0] = splitAdd[0].replace(splitAdd[0][2:], "00")
print(splitAdd)
'''

cleanAddress = []
zipcode = []
lat = []
long = []
regAddress = []


headers = ['regAddress', 'cleanAddress', 'lat', 'long','zipcode']

for values in address_points['features']:
    address = values['properties']['CMPADDABRV']
    try:
        address = address.replace('@', ' ')
        address = address.split()
        address[0] = address[0].replace(address[0][-2:], "00")
        address_txt = ' '.join(address)
        #print(address)
        print(address_txt)
        cleanAddress.append(address_txt)
        zipcode.append(values['properties']['Post_Code'])
        lat.append(values['properties']['Lat'])
        long.append(values['properties']['Long'])
        regAddress.append(values['properties']['CMPADDABRV'])
    except:
        print('something happened')




with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for i in range(len(cleanAddress)):
        content = cleanAddress[i], zipcode[i], lat[i],long[i], regAddress[i]
        writer.writerow(content)

        
    #first split the string
    #replace last two values with zero
    
    # address = address.replace(address[-2:], "00")
    # cleanAddress.append(address)

    #print(values['properties'])



    #print(values['properties']['CMPADDABRV'])
    #print(['properties']['CMPADDABRV'])
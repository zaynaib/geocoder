import json,csv, re

### START CONFIGS ###
cook_geojson = 'Address_Points.geojson'
oemc_locations = 'oemc_locations.csv'
output_file = 'cook_locations.csv'
### END CONFIGS ###

#load the data
address_points = json.load(open(cook_geojson))
#address_points_data = address_points['features']
#print(address_points_data[0])

header_row = ['Add_Number','St_PreDir','St_Name','Post_Code']

cleanAddress = []
address_num = []
address_direction =[]
address_street = []
address_abr = []
zipcode = []
lat = []
long = []
regAddress = []
# now we will open a file for writing
data_file = open(output_file, 'w')
 
 
# create the csv writer object
csv_writer = csv.writer(data_file)

# Writing headers of CSV file
csv_writer.writerow(address_points['features'][0]['properties'].keys()) 
 
for location in address_points['features']:
    
    # Writing data of CSV file
    csv_writer.writerow(location['properties'].values())
 
data_file.close()

print('Done')


"""
given a file with block numbers + street names etc.,
return the same file with a ZIP code field
looked up from the county gis data filei
"""
import json, csv


### START CONFIGS ###
input_file = 'data/oemc.csv'
cook_geojson = 'data/Address_Points.geojson'
output_file_name = 'oemc_locations.csv'
### END CONFIGS ###


# load input file
oemc_columns = ['numerical', 'directional','street_name','suffix']

# for cleaned up location data
output_rows = []



with open(input_file,'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        #grab the oemc street location
        row_location = row['Location']

        location_clean = row_location.replace('@','')

        #split the row location into an array to get the length of the location
        location_split = location_clean.split()

        # some location values are incomplete so nothing to do here
        if len(location_split) < 3:
            continue

        # TODO: validate numerical evaluates to int
        numerical = location_split[0].replace('X','0')
        
        # TODO: validate directional == 1 length & in (NSEW)
        directional = location_split[1]

        # TODO: validate street name is in street name list
        street_name = ' '.join(location_split[2:-1])

        # TODO: validate suffix is in suffix list
        suffix = location_split[-1]
       
        output_row = row
        output_row['numerical'] = numerical
        output_row['directional'] = directional
        output_row['street_name'] = street_name
        output_row['suffix'] = suffix


        output_rows.append(output_row)

# write out
output_file = open(output_file_name,'w')
output_csv = csv.DictWriter(output_file,output_row.keys())
output_csv.writeheader()
output_csv.writerows(output_rows)
output_file.close()



#Logic for code
#split the location column
#replace xx's with 0
#replace @ wtih '' empty string
# check if lengh of split is 4.
# else log the error and mark the row number

# load county gis file into pandas? sql?
# only do this once then save the processed file
# ETL for county 


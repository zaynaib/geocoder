"""
given a file with block numbers + street names etc.,
return the same file with a ZIP code field
looked up from the county gis data filei
"""
import json, csv


### START CONFIGS ###
input_file = 'data/oemc.csv'
cook_geojson = 'Address_Points.geojson'
output_file = 'oemc_locations.csv'
error_output_file = 'outlier_oemc_locations.csv'
### END CONFIGS ###


# load input file
oemc_columns = ['numerical', 'directional','street_name']
oemc_rows = []

with open(input_file,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)

    for row in csvreader:
        #print(row[5])

        #grab the oemc street location
        row_location = row[5]

        #split the row location into an array to get the length of the location
        row_location_split = row_location.split()
        if len(row_location_split) == 4:
            row_location_split[0] = row_location_split[0].replace('X', '0')
            row_location_split[0] = row_location_split[0].replace('@', '')
            oemc_rows.append(row_location_split)


with open(output_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(oemc_columns)
    
    #write the rows of data
    csvwriter.writerows(oemc_rows)



#split the location column
#replace xx's with 0
#replace @ wtih '' empty string
# check if lengh of split is 4.
# else log the error and mark the row number

# load county gis file into pandas? sql?
# only do this once then save the processed file
# ETL for county 


# Geocoder 

Currently the geocoder is specific to 988 data which can be located in the data folder.


data folder
- [oemc.csv](https://docs.google.com/spreadsheets/d/1N5od-Nan0WWpzQLg_7i-wGnzivGCTYXMWXUvFSnONkQ/edit#gid=1894319207)
    
    Raw data of calls made to the Office ofe Emergency Management & Communications. These calls have been marked as releated to a mental health issue.

- Address_Point.geojson

    Geolocations of every address in Cook County. Offical maintenance site of [Address Points](https://hub-cookcountyil.opendata.arcgis.com/datasets/5ec856ded93e4f85b3f6e1bc027a2472_0/about)


Scripts

- oemc_cleanup.py

    This script cleans up and splits the address of the oemc call and splits them into four columns NUMERICAL, DIRECTIONAL, STREET_NAME, SUFFIX 
    EX. 76XX S HALSTED ST becomes 
    
    NUMERICAL: 7600 
    
    DIRECTIONAL: S 
    
    STREET_NAME: HALSTED 
    
    SUFFIX: AVE

    **OUTPUT FILE** - oemc_locations.csv

- geojson_tocsv.py

    Converts Address_Point.geojson into a csv file called **cook_locations.csv**. 
    This was needed for jupyter notebook to read in the data. 


    **OUTPUT FILE** - cook_locations.csv

- geocoding.ipynb

This is a notebook takes an address from *oemc.csv* and finds the zipcode of each address using *cook_locations.csv*.

OUTPUT FILES : geocoded_batches


geocoded_batches

These rows are oemc rows that are geocoded. Meaning that they have a set of zipcodes attached. There will be a set of 30 batches total.



## Workflow

1. Read cook county locations and oemc data files
2. Clean the data
3. Transform the data
4. Extract whatever information that I need
5. Generate file output

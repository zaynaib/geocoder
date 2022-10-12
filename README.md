# Geocoder 

## Purpose of this tool

This tool takes in a spreadsheet of addresses that are located in the city of Chicago and returns geocodeded information such as lat/long and zip code.
Source data set is from Cook County Central website, the dataset is called [Address Points](https://hub-cookcountyil.opendata.arcgis.com/datasets/5ec856ded93e4f85b3f6e1bc027a2472_0/about)


Currently the geocoder is specific to 988 data which can be located in the data folder.

## Folders/ Scripts/Datasets

input folder
- [oemc.csv](https://docs.google.com/spreadsheets/d/1N5od-Nan0WWpzQLg_7i-wGnzivGCTYXMWXUvFSnONkQ/edit#gid=1894319207)
    
    Raw data of calls made to the Office ofe Emergency Management & Communications. These calls have been marked as releated to a mental health issue.

- Address_Point.geojson

    Geolocations of every address in Cook County. Offical maintenance site of [Address Points](https://hub-cookcountyil.opendata.arcgis.com/datasets/5ec856ded93e4f85b3f6e1bc027a2472_0/about)

- src

    Contains scripts to geocoded oemc data. Refer to scripts section of readme for more information.

- notebook

    Contains jupyter notebooks of prototype geocoder scripts.

- output

    Contains geocoded oemc data created from main.py. 



## Scripts

- geocoder.py

    contains a script that can be used with any dataset that needs to be geocoded. It needs 3 columns.
    
    example : 7600  S HALSTED ST

    - Numerical - (street number) 7600
    - Direction -( street direction) S
    - Name - (street name) HALSTED


- helpers.py

    This script contains functions that extract, tranforms, and load oemc data

- cleanup.py

    This script is using the functions from helpers.py to transfrom oemc data in order for it to be ready to be geocoded.

- main.py
    
    This script setup the cleaned oemc data to be geocoded. It returns a csv files of geocoded oemc data.

    **OUTPUT FILE** - oemc_locations2.csv

- geojson_tocsv.py

    Converts Address_Point.geojson into a csv file called **cook_locations.csv**. 
    This was needed for jupyter notebook to read in the data. 


    **OUTPUT FILE** - cook_locations.csv

- geocoding.ipynb

    This is a notebook takes an address from *oemc.csv* and finds the zipcode of each address using *cook_locations.csv*.

    OUTPUT FILES : geocoded_batches


- geocoded_batches_analysis

Exploratory data anaylsis of zipcodes that were geocoded from oemc dataset.



## Workflow

1. Read cook county locations and oemc data files
2. Clean the data
3. Transform the data
4. Extract whatever information that I need
5. Generate file output

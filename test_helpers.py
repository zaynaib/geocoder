from src import helpers
import pytest
import pandas as pd

sample =[
    ("W","WEST"),
    ("E","EAST"),
    ("N","NORTH"),
    ("S","SOUTH"),
    ("apple","APPLE"),
    ("w  ", "WEST")
]

@pytest.mark.parametrize("test_input, expected", sample)
def test_fullDirections(test_input,expected):
    assert helpers.fullDirections(test_input) == expected
    #assert(helpers.fullDirections('W') == 'WEST')


def test_splitUp():
    assert helpers.splitUp('Clark St') == 'Clark'

#create a mock of a dataframe

#create fixture for dataframe

@pytest.fixture
def chicago_location():
    cook_address = pd.read_csv("input/cook_locations.csv")
    return cook_address['CMPADDABRV', 'Lat', 'Long', 'PLACENAME', 'Post_Code', 'OBJECTID','ADDRDELIV','Add_Number','St_PreDir', 'St_Name']

# create a fixture of oemc locations 100 rows
@pytest.fixture
def oemc_data():
    oemc_locations = pd.read_csv("input/oemc_locations.csv")
    return oemc_locations


#refactor extractElement functions

# create a function that does most of the process ???
# maybe it will be too hard to read
#just think about refactoring

def test_head(chicago_location):
    first_five = len(chicago_location.head())
    assert first_five == 5



#test the fullDirections data


def test_geoCodeChunk(chicago_location):
    #here
    pass


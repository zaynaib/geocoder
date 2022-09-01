from src import helpers
import pytest

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
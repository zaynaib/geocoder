import pandas as pd

def fullDirections(direction):
    ''' 

    Takes is direction letter W,E,S or, N and coverts the abbervation to its full name
    Else it will just return the original direction that was provided

    Parameters:
        direction : W, E, S, or N

    Returns:
        WEST,EAST, SOUTH, NORTH or original input
    
    '''

    direction = direction.upper().strip()
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

#create function to split up clean_street_name and then just grab the street name
def splitUp(street):
    '''
    This function just grabs the street name.
   

    Parameters: 
            A string that contains a street name and suffix

            Clark ST

    Returns:
            Street name

            Clark
    '''
    w = street.split(' ')
    return w[0]


def geoCodeChunk(numerical,direction,street_name,database_df):
    '''
    
        example : 7600  S HALSTED ST
        Parameters: 
        Numerical - (street number) 7600
        Direction -( street direction) S
        Name - (street name) HALSTED

        Returns:
        [[60620],[41.75590425],[-87.64385433]]

        TO DO:

        Improve selection criteria from the result set
        Make the result a dictionary instead of a nested list


    '''

    complete_conditional = database_df[(database_df['St_Name'] == street_name) 
                                & (database_df['St_PreDir'] == direction)
                                & (database_df['Add_Number'] < numerical + 100)
                                & (database_df['Add_Number'] >= numerical)
                                ]   
    
    list_zipcodes = list(set(complete_conditional['Post_Code']))
    list_lat = list(set(complete_conditional['Lat']))
    list_long = list(set(complete_conditional['Long']))
    
    
    return [list_zipcodes, list_lat,list_long]



def geoCodeToDf(chunkDfName,columnNamesList):
    '''

    Convert list data structure into a dataframe



    '''
    newDataframe = pd.DataFrame.from_records(chunkDfName, columns=[columnNamesList])
    return newDataframe

#this grabs the list of zipcodes
#extra the raw 
def extractElement(columnList):
    try:
        return columnList[0]
    except:
        return None

#this grabs the first item of list of zipcodes
def extractElement1(columnList):
    try:
        return columnList[0][0]
    except:
        return None
        
#this grabs the first item of list of lats
def extractElement2(columnList):
    try:
        return columnList[1][0]
    except:
        return None


#this grabs the first item of list of longs
def extractElement3(columnList):
    try:
        return columnList[2][0]
    except:
        return None


def extractSpecificElement(columnList,loc1,loc2):

    '''
    
    '''

    try:
        return columnList[loc1][loc2]
    except:
        return None

def toString(elements):
    return list(set([str(x) for x in elements]))
    
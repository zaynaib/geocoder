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


def geoCoder(numerical,direction,street_name,database_df):
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
    '''
    Extracts the first data series from a nested list. In this case the zipcodes

    Example: 
         example_series = [[60620], [41.75590425, 41.75534803, 41.75439881, 41.75583592, 41.75448443, 41.7557676, 41.75522523, 41.7553092, 41.75485436, 41.75575302, 41.75579216, 41.75571389, 41.75583129], [-87.64385433, -87.64383799, -87.64450703, -87.6438536, -87.64450795, -87.64385507, -87.64443377, -87.64443288, -87.64451634, -87.64466506, -87.64466464, -87.64466548, -87.64466422]]
    
    extractElement(example_series)

    returns
        [60620]
    
    '''
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

     Extracts an element from a nested data series.
     For the case of the oemc calls the data structure is :  

     example_series = [[60620], [41.75590425, 41.75534803, 41.75439881, 41.75583592, 41.75448443, 41.7557676, 41.75522523, 41.7553092, 41.75485436, 41.75575302, 41.75579216, 41.75571389, 41.75583129], [-87.64385433, -87.64383799, -87.64450703, -87.6438536, -87.64450795, -87.64385507, -87.64443377, -87.64443288, -87.64451634, -87.64466506, -87.64466464, -87.64466548, -87.64466422]]

     [zip codes, list of lats, list of longs]

     This function extracts a specific element in this nested data structure.

     Example:

     Extract zip code:

     extractSpecificElement(example_series, 0,0)

     returns 60620

     Extract first lat in series:
     extractSpecificElement(example_series,1,0)

     returns 41.75590425

    Extract first lng in series:
    extractSpecificElement(example_series,2,0)

    returns -87.64385433
    '''

    try:
        return columnList[loc1][loc2]
    except:
        return None

def toString(elements):
    '''
    Turns a list/data series into a list of strings
    '''
    return list(set([str(x) for x in elements]))
    
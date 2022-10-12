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
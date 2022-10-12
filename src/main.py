##TO DO:

#refactor to class
#refactor so it can be more usuable with other datasets
#have the option for all of illinois
#have the option for just chicago
#https://stackoverflow.com/questions/2132985/how-to-import-or-include-data-structures-e-g-a-dict-into-a-python-file-from-a

#%%
import pandas as pd
import numpy as np
import math
from helpers import *
from cleanup import chunkDf,database

######  prepare for final output ######

oemc_output = None
oemc_output = pd.DataFrame(columns=['EventNumber', 'EntryDate', 'EventType', 'TypeDescription', 'FinalDisposition', 'Location', 'CPDUnitList', 'CFDUnitList', 'numerical', 'directional', 'street_name', 'suffix' , 'zipcodes','lats','longs','clean_street_name','zipcode_list'])


#test_chunk = chunkDf[0].head()


#%%

def setup(rangeNumStart,rangeNumEnd):
    df = None
    df_complete = None
    for i in range(rangeNumStart,rangeNumEnd):
        df_results = chunkDf[i].apply(lambda x: geoCoder(x["numerical"],x["directional"],x["clean_street_name"],database),axis=1)
        df = df_results.to_frame(name='raw_results')
        codes = df['raw_results'].apply(extractSpecificElement, args =(0,0))
        df['zipcodes'] = codes
    
        lats = df['raw_results'].apply(extractSpecificElement,args =(1,0))
        df['lats'] = lats
    
        longs = df['raw_results'].apply(extractSpecificElement,args = (2,0))
        df['longs'] = longs

        ziplist = df['raw_results'].apply(extractElement)
        df['zipcode_list'] = ziplist
    
        df_complete = pd.concat([chunkDf[i], df], axis=1)
        oemc_output2 = pd.concat([oemc_output,df_complete])

        print('Done')
    return oemc_output2


#%%
'''
#for testing
#%%

#result_setup = setup(0,1)
#end_result = result_setup

#%%
#print(result_setup2)
'''
#%%
result_setup = setup(0,6)

#%%
result_setup2 = setup(6,12)
result_setup3 = setup(12,18)
result_setup4 = setup(18,24)
result_setup5 = setup(24,30)

#%%
end_result = pd.concat([result_setup,result_setup2,result_setup3,result_setup4,result_setup5])
print(len(end_result))
    
#%%
end_result.shape
end_result.head()
#%%
end_result['zipcode_list'] = end_result['zipcode_list'].apply(toString)
end_result.to_csv('../output/oemc_output_data2.csv')


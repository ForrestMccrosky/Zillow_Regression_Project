#############################Function File for Data Acquire############################



from math import sqrt
from scipy import stats
from pydataset import data
from datetime import datetime


from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import sklearn.metrics

import numpy as np
import pandas as pd
import seaborn as sns
from env import host, user, password, sql_connect



def wrangle_zillow():
    '''
    This function is going to acquire the neccessary columns bedroomcnt,
    bathroomcnt, 
    calculatedfinishedsquarefeet, taxvaluedollorcnt, yearbuilt, taxamount, and fips
    from
    the zillow databse in SQL and move it into a pandas dataframe while
    filtering for Single Family Residential properties
    
    The function will then clean the null values by dropping them because the 
    percentage
    of rows with null values was very small compared to the 2.15 million rows of the
    dataframe
    '''
    ## sql query to select the neccessary columns needed for project
    
    ## while using where to filter for homes with the Ids below because those
    ## are considered single family unit homes
    sql_query = '''select * from properties_2017
    join predictions_2017 using(parcelid)
    where transactiondate between "2017-05-01" and "2017-08-31"
    and propertylandusetypeid in (260, 261, 262, 263, 264, 265, 266, 273, 275, 276,
    279)'''
    
    ## Connect to the Zilllow database
    df = pd.read_sql(sql_query, sql_connect('zillow'))    
    
    return df


############################ Organize Zillow #####################

def organize_zillow(df):
    '''
    This function will take in the dataframe for zillow that we have acquired and 
    rename the columns
    '''
    
    ##renaming all the columns to make my life easier
    df = df.rename(columns={
                            'parcelid': 'parcel_id',
                            'calculatedfinishedsquarefeet': 'square_feet',
                            'bathroomcnt': 'baths',
                            'bedroomcnt': 'beds',
                            'taxvaluedollarcnt': 'tax_value',
                            'yearbuilt': 'year_built',
                            'taxamount': 'tax_amount'
    })
    
    return df




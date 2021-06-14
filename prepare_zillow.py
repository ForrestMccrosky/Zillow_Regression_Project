import pandas as pd
import numpy as np
from scipy import stats

import sklearn.preprocessing
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression


def delete_outliers(df):
    '''
    Given the amount of outliers in the data we want to use this function to remove 
    them. 
    
    This function will remove any values that are 3 points outside the 
    absolute value of the z-score
    '''
    ## retains values < 3 z-score of the mean for square_feet column
    trimmed_df = df = df[(np.abs(stats.zscore(df['square_feet'])) < 3)]
    
    ## retains values < 3.5 z-score of the mean for baths column
    trimmed_df = df[(np.abs(stats.zscore(df['baths'])) < 3)]
    
    ## retains values < 3.5 z-score of the mean for beds column
    trimmed_df = df[(np.abs(stats.zscore(df['beds'])) < 3)]
    
    ## retains values < 3.5 z-score of the mean for tax_value column
    trimmed_df = df[(np.abs(stats.zscore(df['tax_value'])) < 3)]
    
    return trimmed_df


############################## Split function #########################

def split_data(df):
    '''
    This function takes in a datframe and split it into the 
    train, validate, and test dataframes neccessary for proper modeling
    '''
    # Create train_validate and test datasets
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123)
    # Create train and validate datsets
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=123)

    return train, validate, test

############################## Min, Max Scaler function from Curriculumn #########################


def Min_Max_Scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    Returns scaler, X_train_scaled, X_validate_scaled, X_test_scaled dfs 
    """
    scaler = sklearn.preprocessing.MinMaxScaler().fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index,     
                                     columns= X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled
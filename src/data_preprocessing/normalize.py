"""
Created on Mon Nov 13 12:28:24 2017

@author: Erik
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import summary

def normalize(iData):

    
    iData = add_yn_feature(iData, 'HasLotFrontage', 'LotFrontage')
    iData = add_yn_feature(iData, 'HasBsmt', 'TotalBsmtSF')
    iData = add_yn_feature(iData, 'HasPool', 'PoolArea')
    iData = add_yn_feature(iData, 'HasGarage', 'GarageArea')
    
    iData = take_logs(iData)
 
    
    #unnecessary features
    iData = iData.drop('MiscFeature', 1)
    iData = iData.drop( 'MiscVal', 1)
    
    #add 0 1 encoding
    iData = pd.get_dummies(iData)
    
    remove_correlated_features(iData)
    
    return iData

def take_logs(iData):
    iData = take_log(iData, 'SalePrice')
    iData = take_log(iData, 'GrLivArea')
    iData = take_log(iData, '1stFlrSF')
    return iData
    
    
def remove_correlated_features(iData):
    #highly correlated with greatliveara
    
    iData = iData.drop('TotRmsAbvGrd', 1)
    
    #highly correlated with Garage area
    iData = iData.drop('GarageCars', 1)
    
    #highly correlated with year built
    iData = iData.drop('GarageYrBlt', 1)
    
    iData = iData.drop('TotalBsmtSF', 1)
    
    return iData



def fill_in_missing_values(iData):
    values = {}
    col_type_list = summary.missing_data(iData)
    for index, row in col_type_list.iterrows():
        if (row.Total == 0):
            break
        #if(index == 'LotFrontage'):
            #values[index] = 69.79
        if(row.DataType == 'object'):
            values[index] = 'NotApplicable'
        else:
            values[index] = 0
    
    return iData.fillna(value = values)
        

def add_yn_feature(iData, feature, based_on):
    #creates feature with your feature name that has a value of 1 where
    # the based on feature is greater than  0
    iData[feature] = pd.Series(len(iData[based_on]), index=iData.index)
    iData[feature] = 0 
    iData.loc[iData[based_on]> 0,feature] = 1
    return iData

def take_nonzero_log(iData, feature):
    temp = iData.loc[iData[feature]>0]
    iData.loc[iData[feature]>0,feature] = np.log(temp[feature])
    
    return iData
    
def take_log(iData, feature):
    iData[feature] = np.log(iData[feature])
    iData = iData.rename(columns = {feature: 'log_' + feature})
    return iData
    
    
def drop_cols_with_missing_data(iData):
    total = iData.isnull().sum().sort_values(ascending=False)
    percent = (iData.isnull().sum()/iData.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    iData = iData.drop(iData.loc[iData['Electrical'].isnull()].index)
    return iData.drop((missing_data[missing_data['Total'] >= 8]).index,1)
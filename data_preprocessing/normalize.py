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
    iData = take_log(iData, 'SalePrice')
    iData = take_log(iData, 'GrLivArea')
    
    iData = add_yn_feature(iData, 'HasBsmt', 'TotalBsmtSF')
    
    iData = take_nonzero_log(iData, 'TotalBsmtSF', 'HasBsmt')

    #very dangerous, removes entire column if 1 record is missing.  Use with cuation.
    iData = drop_cols_with_missing_data(iData)    
    
    iData = drop_column(iData, 'MiscFeature')
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
    iData[feature] = pd.Series(len(iData[based_on]), index=iData.index)
    iData[feature] = 0 
    return iData

def take_nonzero_log(iData, feature, yn_feature):

    iData.loc[iData[feature]> 0,yn_feature] = 1
    temp = iData.loc[iData[yn_feature]==1]
    iData.loc[iData[yn_feature]==1,feature] = np.log(temp[feature])
    return iData
    
    
def take_log(iData, feature):
    iData[feature] = np.log(iData[feature])
    return iData
    
    
def drop_column(iData, feature):
    return iData.drop(feature, 1)

def drop_cols_with_missing_data(iData):
    total = iData.isnull().sum().sort_values(ascending=False)
    percent = (iData.isnull().sum()/iData.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
    return iData.drop((missing_data[missing_data['Total'] >= 1]).index,1)
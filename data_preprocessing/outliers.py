# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:59:59 2017

@author: Erik
"""

def remove_outliers(iData):

    #df_train.sort_values(by = 'GrLivArea', ascending = False)[:2]
    iData = iData.drop(iData[iData['Id'] == 1299].index)
    iData = iData.drop(iData[iData['Id'] == 524].index)
    return iData
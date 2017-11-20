# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:59:59 2017

@author: Erik
"""

def remove_outliers(iData):

    #based on GrLivArea
    iData = iData.drop(iData[iData['Id'] == 1299].index)
    iData = iData.drop(iData[iData['Id'] == 524].index)
    
    #based on lot frontage, anything with value > 300 removed
    iData = iData.drop(iData[iData['Id'] == 935].index)
    
    #based on lot area, anything with value > 100,000 removed
    iData = iData.drop(iData[iData['Id'] == 250].index)
    iData = iData.drop(iData[iData['Id'] == 314].index)
    iData = iData.drop(iData[iData['Id'] == 336].index)
    iData = iData.drop(iData[iData['Id'] == 707].index)
    iData = iData.drop(iData[iData['LotArea'] >55000].index)

    #based on sale price, anything with a value over 600,000
    iData = iData.drop(iData[iData['Id'] == 692].index)
    iData = iData.drop(iData[iData['Id'] == 899].index)
    iData = iData.drop(iData[iData['Id'] == 1170].index)
    iData = iData.drop(iData[iData['Id'] == 1183].index)
    
    

    return iData
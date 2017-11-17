# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:56:03 2017

@author: Erik
"""

import summary
from outliers import remove_outliers
from normalize import normalize, fill_in_missing_values
import pandas as pd

df_train = pd.read_csv('train.csv')


print(summary.missing_data(df_train))

df_train = fill_in_missing_values(df_train)
df_train = remove_outliers(df_train)

print(summary.missing_data(df_train))
summary.scatter_plot(df_train, 'LotFrontage', 'SalePrice')

#for col, dtype in summary.columns_and_types(df_train):
#    if(dtype == 'object'):
#        summary.box_whisker_plot(df_train, col, 'SalePrice')
#    else:
#        summary.scatter_plot(df_train, col, 'SalePrice')
        

#dfTrain = normalize(dfTrain)




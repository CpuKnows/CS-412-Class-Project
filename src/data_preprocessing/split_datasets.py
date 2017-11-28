# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:59:59 2017

@author: John
@tldr: Splits the AmesHousing dataset and the version with geodemos into 
		training and test sets. Ensures similar SalePrice quantiles between 
		the original dataset, training set, and test set
"""

import numpy as np
import pandas as pd

# Splitting dataset
print('Splitting AmesHousing dataset')
ames_data = pd.read_csv('../data/input/AmesHousing_with_latlon.csv')

# Split dataset 80/20
train, test = train_test_split(ames_data, test_size=0.2, random_state=12)
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Ensure quantiles are similar
a = ames_data['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))
b = train['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))
c = test['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))

quantiles = pd.concat([a,b,c], axis=1)
quantiles.columns = ['OrigPrice', 'TrainPrice', 'TestPrice']
quantiles['TrainDiff'] = quantiles['OrigPrice'] - quantiles['TrainPrice']
quantiles['TestDiff'] = quantiles['OrigPrice'] - quantiles['TestPrice']

print('Train diff total:', np.sum(np.abs(quantiles['TrainDiff'].values)))
print('Test diff total:', np.sum(np.abs(quantiles['TestDiff'].values)))
print()
print('Quantiles')
print(quantiles)
print()

# Save train and test sets
train.to_csv('../data/input/ames_train.csv', index=False)
test.to_csv('../data/input/ames_test.csv', index=False)

# Splitting geodemo dataset
print('Splitting AmesHousing dataset with geodemos')
ames_data = pd.read_csv('../data/input/AmesHousing_with_geodemo.csv')

# Split dataset 80/20
train, test = train_test_split(ames_data, test_size=0.2, random_state=12)
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Ensure quantiles are similar
a = ames_data['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))
b = train['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))
c = test['SalePrice'].quantile(np.arange(0.1, 1.0, 0.1))

quantiles = pd.concat([a,b,c], axis=1)
quantiles.columns = ['OrigPrice', 'TrainPrice', 'TestPrice']
quantiles['TrainDiff'] = quantiles['OrigPrice'] - quantiles['TrainPrice']
quantiles['TestDiff'] = quantiles['OrigPrice'] - quantiles['TestPrice']

print('Train diff total:', np.sum(np.abs(quantiles['TrainDiff'].values)))
print('Test diff total:', np.sum(np.abs(quantiles['TestDiff'].values)))
print()
print('Quantiles')
print(quantiles)

# Save train and test sets
train.to_csv('../data/input/ames_geodemo_train.csv', index=False)
test.to_csv('../data/input/ames_geodemo_test.csv', index=False)

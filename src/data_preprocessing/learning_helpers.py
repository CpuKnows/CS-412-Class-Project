# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:47:45 2017

@author: Erik
"""
from sklearn.metrics import r2_score

def greedy_feature_selection(learner, X_train, y_train, X_test, y_test,tolerance = 0.00001, debug = False):
    unselected_features = list(X_train)
    selected_features = []
    accuracy = 0
    while(True):
        max_model_accuracy = 0
        best_feature = None
        for col in unselected_features:
            learner.fit(X_train[selected_features + [col]], y_train)
            y_geo_pred = learner.predict(X_test[selected_features + [col]])
            model_accuracy = r2_score(y_test, y_geo_pred)
            if(model_accuracy > max_model_accuracy):
                best_feature = col
                max_model_accuracy = model_accuracy
        if(debug == True):
            print(best_feature)
            print(max_model_accuracy)
        selected_features.append(best_feature)
        unselected_features.remove(best_feature)
        if(model_accuracy - accuracy < tolerance):
            break
        else:
            accuracy = model_accuracy
    learner.fit(X_train[selected_features], y_train)
    y_pred = learner.predict(X_test[selected_features])
    return learner, selected_features, r2_score(y_test, y_pred)
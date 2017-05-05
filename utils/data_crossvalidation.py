from __future__ import  division
import random
import math
import numpy as np

def shuffle_data(X , y , seed = None):
    # merge X and target(Y)
    data =np.concatenate((X, y.reshape((1, len(y))).T), axis=1)
    np.random.shuffle(data)
    return (data[:,:-1] , data[:,-1].astype(int))

def split_dataset(X ,y , split_ratio = 0.7 , shuffle = True , seed = 1234):
    if shuffle:
        shuffle_data(X ,y , seed)
     # Split data into training and test set based on split ratio
    split_end = len(y) - int(len(y) // (1/ split_ratio))
    X_train , X_test = X[:split_end] , X[split_end:]
    y_train , y_test =  y[:split_end] , y[split_end:]

    return (X_train , X_test , y_train , y_test)
def separated_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        row = dataset[i]
        if (row[-1] not in separated):
            separated[row[-1]] = []
        separated[row[-1]].append(row)
    return separated

'''
K Nearest neighbour (k-NN) Classifier
author: Chandan Saha
'''

import sys
import os
from sklearn import  datasets # Using standard datasets
import  numpy as np
from sklearn.decomposition import  pca
import matplotlib.pyplot as plt
from sklearn.metrics import  accuracy_score


#import uitlity functions
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/../utils/')
try:
    from data_stats import  euclidean_distance
    from data_crossvalidation import split_dataset
except ImportError as e:
    print("Import Error", e.args)


class KNN():
    '''
    :param : k : int  NUmber of closest number
    '''
    def __init__(self , k = 5):
        self.k = k
    def majority_voting(self , neighbors , classes):
        max_count = 0
        common = 0
        # check number of closest neighbor
        for count in np.unique(classes):
            #count
            cnt = len(neighbors[neighbors[:,1] == count])
            if max_count < cnt:
                max_count =cnt
                common = cnt
        return common
    def predict(self , X_train,X_test,y_train):
        classes = np.unique(y_train)
        y_prediction = list()
        for test_instance in X_test:
            neighbors = list()
            # Determine classes of each instance based on distance
            for j ,observered_instance in enumerate(X_train):
                dist = euclidean_distance(observered_instance , test_instance)
                label = y_train[j]
                #add neighbor information
                neighbors.append([dist , label])
            neighbors = np.array(neighbors)

            # Sort based on distance in descending order
            k_nearest_neightbor = neighbors[neighbors[:,0].argsort()][:self.k]

            label = self.majority_voting(k_nearest_neightbor , classes)

            y_prediction.append(label)

        return np.array(y_prediction)
def main():
    iris = datasets.load_iris()
    #print(iris.data[1:5])

    X =iris.data
    y = iris.target
    # Training and Test Split
    X_train , X_test , y_train , y_test = split_dataset(X,y,split_ratio = 0.7,seed = 1256)
    #print("Training",X_train[1:5,])
    #print("Testing",X_test[1:5])

    clf = KNN(k = 3)
    y_prediction = clf.predict(X_train , X_test , y_train)
    print(y_test , y_prediction)
    accuracy = accuracy_score(y_test , y_prediction)

    print ("Accuracy:" , accuracy)


if __name__ == '__main__':
    main()

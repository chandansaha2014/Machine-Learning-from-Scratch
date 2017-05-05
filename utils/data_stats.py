import math
import numpy as np
from sklearn import datasets

# class Stats(object):
#     def __init__(self):
#         self.p = 2
def euclidean_distance(x1 , x2 , *args):
    dist = 0
    #for index in range(len(x1)):
    dist = np.linalg.norm(x1-x2)
    return dist




# test
# data = datasets.load_iris()
# print(data)
#
# edist = Stats.euclidean_distance(data[0] , data[1])
# print(edist)

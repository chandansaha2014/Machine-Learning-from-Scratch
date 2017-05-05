import math
import numpy as np


class Stats():
    def euclidian_distance(self , x1 , x2 , *args):
        dist = 0
        #for index in range(len(x1)):
        dist = np.linalg.norm(x1-x2)
        return dist

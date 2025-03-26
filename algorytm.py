import pandas as pd
import numpy as np
from itertools import combinations


def load(file):
    data = np.loadtxt(file, dtype="int", delimiter=" ")
    return data


def exhaustive_algorithm(data):
    number_of_objects = (data.shape)[0]
    number_of_atributes = data.shape[1]-1
    decision_index = data.shape[1]-1
    # i_matrix = np.zeros((number_of_objects,number_of_objects))
    i_matrix = [[""]*number_of_objects]*number_of_objects
    # print(i_matrix)

    for object in range(number_of_objects):
        for atribute in range(number_of_atributes):
            for object2 in range(object+1, number_of_objects):
                is_equal = 1
                # print("object:" + str(object+1) + " " + "object2:" + str(object2+1))
                if data[object][decision_index] == data[object2][decision_index]:
                    # print("Is equal")
                    for i in range(number_of_atributes):
                        if data[object][i] == data[object2][i]:
                            is_equal = 1
                            i_matrix[object][object2] += "a"+str(atribute)
                        else:
                            is_equal = 0
                else:
                    pass
                    # print("Not equal")

    return i_matrix



data = load("values.txt")
exhaustive_algorithm(data)
print(exhaustive_algorithm(data))
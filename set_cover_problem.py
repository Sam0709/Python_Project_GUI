import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from itertools import *
import numpy as np
import random

def function():
    dataset = pd.read_csv(r'C:\Users\shami\Desktop\venv\greddy.csv')
    print(dataset)
    # print(dataset.shape)
    # print(dataset.describe())
    # print(dataset[["39"]]) #dataset.iloc[0]

    k = dataset.iloc[0]
    k1 = dataset.iloc[:, 0]

    row = len(k)
    column = len(k1)
    print(row)
    print(column)

    m = []  # init the first level
    for i in range(column):
        m.append([])  # init m[i]
        y = 0
        for j in (dataset.iloc[i]):
            y = y + 1
            if j == 1:
                m[i].append(y - 1)


    m1=[]
    for i in (m):
        g=set(i)
        m1.append(g)

    return m1

print(function())


def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    elements = set(e for s in subsets for e in s)
    # Check the subsets cover the universe
    if elements != universe:
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset

    return cover


def main():
    universe = set(range(1, 46))
    subsets = function()
    cover = set_cover(universe, subsets)
    print(cover)


if __name__ == '__main__':
    main()


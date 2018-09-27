#!usr/bin/env python
# -*- coding：UTF-8-*-

import numpy as ny
import operator
def classify0(inX,dataSet,labels,k):
    dataSetsize=dataSet.shape[0]
    diffMat=ny.tile(inX,(dataSetsize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
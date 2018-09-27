#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import svmutil as sm
import numpy as np
import grid


def loadDataSet(fileName):
    dataMat=[];labelMat=[]
    with open(fileName) as fr:
        for line in fr.readlines():
            lineArr=line.strip().split('\t')
            dataMat.append([float(lineArr[0]),float(lineArr[1])])
            labelMat.append(float(lineArr[2]))
    return dataMat,labelMat
def testdata(trainfilename,testfilename):

    dataArr1, labelArr1 = loadDataSet(trainfilename)
    dataArr2, labelArr2 = loadDataSet(testfilename)
    errorCount = 0
    arg=['-s',0,'-t',2,'-c',0.031,'-g',0.0078]
    model = sm.svm_train(labelArr1, dataArr1, arg)
    [plabel, pacc,pval]=sm.svm_predict(labelArr2,dataArr2,model)

if __name__=='__main__':
    trainfilename='C:/Users/XUEJW/Desktop/dataset/MLiA_SourceCode/machinelearninginaction/Ch06/testSetRBF.txt'
    testfilename='C:/Users/XUEJW/Desktop/dataset/MLiA_SourceCode/machinelearninginaction/Ch06/testSetRBF2.txt'
    #testdata(trainfilename,testfilename)
    grid.find_parameters(trainfilename)




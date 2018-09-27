#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import operator
from math import log
def getrow(Data,n):#取某列
    Alist=[]
    for aline in Data:
        if n > len(aline):
            print('larger than Data!')
        else:
            Alist.append(aline[n])
    return Alist
def splitData(Data,i,val):#将i列是val值的行，取出余下列表
    col=[]
    pcol=[]
    for lt in Data:
        if lt[i]==val:
            pcol=lt[:i]
            pcol.extend(lt[i+1:])
            col.append(pcol)
    return col
def Shannon(Data):#计算香浓值
    dicts={}
    ln=len(Data)
    sums=0
    Labellist=getrow(Data,-1)
    bln=len(Labellist)
    for label in Labellist:
        dicts[label]=dicts.get(label,0)+1
    for key in dicts:
        prob=dicts[key]/ln
        sums-=prob*log(prob,2)
    return sums
def chooseShannonFeature(Data):#根据香浓求出最佳的分类元素，按哪一列元素划分，香浓值最小
    fentropy=0.0
    entropy=0.0
    ln=len(Data[0])-1
    dic={}
    fdic={}
    for i in range(ln):
        alist=getrow(Data,i)
        slist=set(alist)
        for v in slist:
            num=alist.count(v)
            nlist=splitData(Data,i,v)
            pentropy=Shannon(nlist)
            entropy+=num*pentropy/len(Data)
        if fentropy==0.0 or fentropy > entropy:
            fentropy=entropy
            bestfeature=i

        dic[i]=fentropy
        fdic=sorted(dic.items(),key=operator.itemgetter(1))
    return bestfeature
def majorityCnt(classList):#最后就剩一个分类时标签不一致，取最多出现者
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        else:
            classCount[vote]+=1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
def createTree(dataSet,labels):#ID3算法
    classList=[cell[-1] for cell in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseShannonFeature(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues=[cell[bestFeat] for cell in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitData(dataSet,bestFeat,value),subLabels)
    return myTree
def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'wb+')#必须二进制
    pickle.dump(inputTree,fw)
    fw.close()
def grabTree(filename):
    import pickle
    fr=open(filename,'rb')
    return pickle.load(fr)

if __name__=='__main__':
    Data = [[1, 1, 'yes'],  [1, 1, 'yes'],[1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    label1=['no surfacing','flippers']

    myTree=createTree(Data,label1)

    storeTree(myTree,'shannontest.txt')
    print(grabTree('shannontest.txt'))
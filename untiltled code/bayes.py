#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import math
def bayes(ybdata,label,indata1):
    ln=len(label)
    indata=set(indata1)
    ln2=len(indata)
    ddic=outdic=outdic1={}
    temp=1
    Psum=0
    for x in range(ln):
        lx=label[x]
        if lx not in ddic:
            ddic[lx]=ybdata[x]
        else:
            ddic[lx].extend(ybdata[x])
    for k in ddic:
        for c in indata:
            #temp *= (ddic[k].count(c)+1)
            if ddic[k].count(c)!=0:
                temp*=(ddic[k].count(c))
            else:
                temp *= (ddic[k].count(c)+0.1)
        outdic[k]=temp*(label.count(k)/float(ln))/(len(ddic[k])**ln2)

        Psum+=outdic[k]

    for k1 in outdic:
        outdic1[k1] = outdic[k1]/ float(Psum)
        #outdic1[k1]=math.log(outdic[k1])/float(Psum)
       # print(outdic1[k1])
    return outdic1

if __name__=='__main__':
    ybdata = [['my','dog','has','flea','problems','help','please'],
              ['maybe','not','take','him','to','dog','park','stupid'],
              ['my','dalmation','is','so','cute','i','love','him'],
              ['stupid','worthless','garbage'],
              ['mr','licks','ate','my','steak','how','to','stop','him'],
              ['quit','buying','worthless','dog','food','stupid']]
    label=['a','b','a','b','a','b']
    testlist1=['my','dog','garbage','stupid','so','worthless','stop','not']
    testlist2=['stupid','garbage']
    resout=bayes(ybdata,label,testlist2)
    print(resout)

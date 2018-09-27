#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
class Cname:
    def __init__(self,element,ref):
        self.title=element
        self.ref=ref
def loaddata(inData,k):
    celldict={}
    popdict={}
    outdict={}
    finaldict = {}
    num=0
    for item in  inData:
        if item!=[]:
            for cell in item:
                if cell in celldict:
                    celldict[cell]+=1
                else:
                    celldict[cell]=1
    outlist=sorted(celldict.items(),key=lambda p:p[1],reverse=True)
    #print('out:',outlist)
    for keys in outlist:
        kt = Cname(keys[0], keys[1])
        #print('kt:',keys)
        if k==0:
            if keys[1]<100000:
                popdict[keys[0]]=keys[1]
            else:
                outdict[kt]=[]
        else:
            outdict[kt] = []
    #print('di:',celldict)
    for item in inData:
        refcell=0
        output=[]
        changed=0
        title=Cname(None,None)
        if item!=[]:
            #print('item:',item)
            num=1
            for cell in item:
                if k==0:
                    if cell not in popdict:
                        #print('c:', cell, output)
                        output.append(cell)
                else:

                    output.append(cell)
                if celldict[cell]>refcell:
                    refcell=celldict[cell]
                    maxn=cell
                    changed=1
            if changed==1 and output!=[]:
                #print('s:',output,'\n',maxn)
                output.remove(maxn)
                for keys in outdict:
                    if keys.title==maxn:
                        #print('p:', tin)
                        outdict[keys].append(output)
                #print('tit:',title.title+':'+str(title.ref))
        #if output!=[]:


                #outdict[maxn].append(output)


    for items in outdict:
        if outdict[items]!=[]:
            finaldict[items]=outdict[items]

    #print('2:',finaldict)
    for item in finaldict:
        finaldict[item]=loaddata(finaldict[item],1)
        if num==0:
            break


    return finaldict


def creatTree(inputData,k):
    for item in inputData:
        if inputData[item]==[]:
            num=0
            continue
        else:
            #print('i:',item,input[item])
            num=1
            inputData[item]=loaddata(inputData[item],k)
    return inputData,num

def printtree(tree):
    prtree={}
    for item in tree:
        #print('dic2:',type(tree[item]))
        rna=item.title+'->'+str(item.ref)
        prtree[rna]=tree[item]
        if type(tree[item])==dict:
            #print('dic:','d')
            prtree[rna]=printtree(tree[item])
    return prtree





if __name__ == '__main__':
    indata = [['r','z','j','h','p'], ['z','y','x','w','v','u','t','s'],['z'], ['r','x','n','o','s'], \
              ['y','r','x','z','q','t','p'],['y','z','x','e','q','s','t','m']]
    kosarak=[line.split() for line in open('C:/Users/XUEJW/Desktop/dataset/MLiA_SourceCode/machinelearninginaction/Ch12/kosarak.dat').readlines(100)]
    #print('d:',kosarak)
    rodata=loaddata(kosarak,0)
    df=printtree(rodata)
    print(df)

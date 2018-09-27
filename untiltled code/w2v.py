#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import csv
import jieba

import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import Word2Vec
from gensim.models import word2vec
def w2v_csv():
    csvFile = open(r"C:\Users\XUEJW\Desktop\兴业数据\test.csv", "r",encoding='UTF-8')
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    data = []
    sentences =word2vec.Text8Corpus(r"C:\Users\XUEJW\Desktop\兴业数据\test.txt")  # 加载语料
    # print(list(sentences))
    for item in reader:
        if len(item)>0:
            #print('0',item,type(item))
            for cell in item:
                cell.strip()
                #print('1:',cell)
                data.append([cell])
    print(data)

    model = Word2Vec(data, sg=1, size=3,  window=2,  min_count=1, sample=0.001)
    model.wv.save_word2vec_format(r'C:\Users\XUEJW\Desktop\兴业数据\mymodel.txt',binary=False)
    model.save(r'C:\Users\XUEJW\Desktop\兴业数据\mymodel')

    # model = Word2Vec.load(r'C:\Users\XUEJW\Desktop\兴业数据\mymodel1')
    # model.train(data,total_examples=model.corpus_count,epochs=model.epochs)
    # model.save(r'C:\Users\XUEJW\Desktop\兴业数据\mymodel1')
    csvFile.close()
def w2v_test():
    raw_sentences = ['拍照 反光 一直 是 摄影 爱好者 较为 苦恼 的 问题',
    '尤其 是 手机 这种 快速 拍照 设备 的 成像 效果 总是 难以 令人 满意',
    '特别 是 抓拍 的 珍贵 照片',
    '遇上 反光 照片 基本 作废',
    '而 索尼 最近 研发 的 集成 偏振片 传感器',
    '似乎 可以 有效 的 解决 拍照 反光 的 问题']
    sentences = [s.split() for s in raw_sentences]
    model = word2vec.Word2Vec(sentences, min_count=1)
    mod = Word2Vec.load(r'Word60.model')  # 3个文件放在一起：Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy
    fout = open(r"字词相似度.txt", 'w')
    for word in showWord:
        if word in mod.index2word:
            sim = mod.most_similar(word)
            fout.write(word + '\n')
            for ww in sim:
                fout.write('\t\t\t' + ww[0] + '\t\t' + str(ww[1]) + '\n')
            fout.write('\n')
        else:
            fout.write(word + '\t\t\t——不在词汇表里' + '\n\n')

    fout.close()
    print(model.most_similar('手机'))
# w2v_csv()
w2v_test()
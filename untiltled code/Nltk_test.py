#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import nltk
from nltk.parse import stanford#要写绝对路径的环境
import os
stanford_parser_path=r'D:/stanford_nlp/stanford-parser-full-2015-12-09/stanford-parser.jar'#要绝对路径
stanford_model_path=r'D:/stanford_nlp/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
os.environ['STANFORD_PARSER']=stanford_parser_path
os.environ['STANFORD_MODELS']=stanford_model_path
os.environ['JAVAHOME']=r'C:\Progra~1\Java\jdk1.8.0_131'
string1=r'D:/stanford_nlp/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models/'
model_path=os.path.join(string1,'edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz')
parser=stanford.StanfordParser(model_path=model_path)#model下有个专门的中文，更大更详细,这是句法分析

if __name__ == '__main__':
    # words = nltk.word_tokenize('i hate study on monday. Jim like rabbit. ')#分词一句话，结果是list,标点符号也会分出来
    #
    # fd = nltk.FreqDist(words)#统计词频
    # for x, y in fd.items():
    #     print(type(x), type(y), x, y)
    # # < class 'str'> < class 'int' > i 1
    # english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    #
    # words = [word for word in words if word not in english_punctuations]#还可以用string去标点
    #
    #
    # pos = nltk.pos_tag(words)#词性标注，返回list，元素是tuple，标点的词性还是标点
    # ner=nltk.ne_chunk(pos)#实体标注，输入得是词性标注的结果，返回是树，可以print
    # for x in ner:
    #     # print(x,type(x),x[0],type(x[0]))
    #     print(type(x))
    #     if type(x) == nltk.tree.Tree:#如何实体有被识别则是树，否则就是tuple（即pos的结果）
    #         print('ok')
    # print('words:',words)

    # sentences=parser.raw_parse('i am jeffyang')
    sentences=parser.raw_parse('我 是 杨晓君')
    print('0:',sentences)
    for x in sentences:
        print('1:',x)
        # x.draw()
    sentences = parser.raw_parse('i am jeffyang')#要加载英文的model_path
    for x in sentences:
        print('2:',x)
        # x.draw()

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import os
import sys
import codecs
import chardet
add=r'E:\gdl'
for (root,dirs,files) in os.walk(add):
    for item in files:
        ff = codecs.open(add+'\\'+item, 'rb').read()
        fs = chardet.detect(ff)['encoding']
        content = ff.decode(fs).encode('utf-8')
        codecs.open(add+'\\'+item, 'w').write(content)
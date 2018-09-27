#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
from xmlrpc.server import SimpleXMLRPCServer as rpc#只能传输
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import KeyedVectors
w2v_model = './news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
try:
    print('loading data...')
    model = KeyedVectors.load_word2vec_format(w2v_model, binary=True)
    print('Data loaded.')
except Exception as e:
    print('err:', e)


class test:
    def find_from_w2v(self,instr):  # word2vec
        global model
        index = model.wv.index2word
        out_data = []
        if instr in index:
            rela_word = model.most_similar(instr, topn=3)  # is a list
            # print('te6:',rela_word)
            for xw in rela_word:
                out_data.append(xw[0])
            return tuple(out_data)

if __name__ == '__main__':
    server = rpc(("localhost", 8080))

    print("Listening on port 8080...")

    server.register_introspection_functions()
    server.register_multicall_functions()

    server.register_instance(test())

    # s.register_function(is_even,"is_even")
    # s.register_function(pp,"pp")
    server.serve_forever()
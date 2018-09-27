#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
def getFileLineNums(filename):#统计有多少个向量
    f = open(filename, 'r')
    count = 0

    for line in f:
        count += 1
    return count


# def prepend_line(infile, outfile, line):
#     """
#     Function use to prepend lines using bash utilities in Linux.
#     (source: http://stackoverflow.com/a/10850588/610569)
#     """
#     with open(infile, 'r') as old:
#         with open(outfile, 'w') as new:
#             new.write(str(line) + "\n")
#             shutil.copyfileobj(old, new)


def prepend_slow(infile, outfile, line):
    """
    Slower way to prepend the line by re-creating the inputfile.
    """
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            fout.write(line + "\n")
            for line in fin:
                fout.write(line)

def load(filename):#修改glove的模型文件，从而可以用word2vec加载

    # Input: GloVe Model File
    # More models can be downloaded from http://nlp.stanford.edu/projects/glove/
    # glove_file="glove.840B.300d.txt"
    glove_file = filename

    dimensions = 300

    num_lines = getFileLineNums(filename)
    # num_lines = check_num_lines_in_glove(glove_file)
    # dims = int(dimensions[:-1])
    dims = 300

    # print(num_lines)
    #
    # # Output: Gensim Model text format.
    gensim_file = 'glove_model.txt'
    gensim_first_line = "{} {}".format(num_lines, dims)
    #
    # # Prepends the line.
    # if platform == "linux" or platform == "linux2":
    #     prepend_line(glove_file, gensim_file, gensim_first_line)
    # else:
    #     prepend_slow(glove_file, gensim_file, gensim_first_line)
    prepend_slow(glove_file, gensim_file, gensim_first_line)
        # Demo: Loads the newly created glove_model.txt into gensim API.
    # model = gensim.models.Word2Vec.load_word2vec_format(gensim_file, binary=False)  # GloVe Model
    #
    # model_name = filename[5:-4]
    #
    # model.save('model\\' + model_name)

    # return model
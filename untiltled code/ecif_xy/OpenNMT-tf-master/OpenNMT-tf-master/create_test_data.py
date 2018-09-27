# This script is writen for generating a samples to validate NMT to predicting
import random
# parameter settings
# note that the train number should be 100times than vocabulary number.
param_train_num = 100
param_test_num = 100
param_val_num = 100
param_vocab_num = 1000
param_history_window_size = 15
param_predict_window_size = 1
param_prefix = 't_'
param_split_portion = 0.8
param_test_history_window_size = 5

#  define some necessary files for NMT
src_test = open('src-test.txt','w')

# get data set from file
f = open('environment.csv')
num_list = []
for line in f:
    num = line.split(',')
    num_list.append(num[1].replace("\n", ""))

# split data set to train_list ,test_list and validation_list
test_list = num_list

# create test data
for i in range(len(test_list)-param_test_history_window_size):
    src_str = ''
    for j in range(param_test_history_window_size):
        src_str = src_str + ' ' + test_list[i+j]
    src_test.write(src_str + '\n')


# restore resource and close session for security
src_test.close()

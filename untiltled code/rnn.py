#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)
init_size=784
batch_size=100
input_size=28
n_steps=28#28x28=784
n_hidden=128
n_output=10

x=tf.placeholder(tf.float32,[None,n_steps,input_size])
y=tf.placeholder(tf.float32,[None,n_output])


def getinput(x_init):

    #x_init_reshape=np.reshape(x_init,[batch_size,n_steps,input_size])
    change_x=tf.reshape(x_init,[-1,input_size])
    W_x_init=tf.Variable(tf.truncated_normal([input_size,n_hidden],stddev=0.1))#tf.random_normal([input_size,n_hidden])
    b_x_init=tf.Variable(tf.constant(0.1,shape=[n_hidden,],dtype=tf.float32))
    get_x=tf.matmul(change_x,W_x_init,name='X_in')+b_x_init#[batch_size*n_step,n_hidden]
    return get_x
def rnn_cell(get_x):#for every input_size,need[batch_size,n_step,n_hidden]
    cell_x=tf.reshape(get_x,[batch_size,n_steps,n_hidden])
    lstm_cell=tf.nn.rnn_cell.BasicLSTMCell(n_hidden,state_is_tuple=True)
    state_init=lstm_cell.zero_state(batch_size,dtype=tf.float32)
    outputs,state=tf.nn.dynamic_rnn(lstm_cell,cell_x,initial_state=state_init,time_major=False)
    #outputs=[batch_size,n_step,n_hidden],state=[batch_size,n_hidden]
    return state

# def makernn():
#     pass
def getoutput(state):
    W_output=tf.Variable(tf.truncated_normal([n_hidden,n_output],stddev=0.1))
    b_output=tf.Variable(tf.constant(0.1,shape=[n_output,],dtype=tf.float32))
    results=tf.matmul(state[1],W_output)+b_output
    return results

def RNN(x_init):
    get_x=getinput(x_init)
    rnn_state=rnn_cell(get_x)
    results=getoutput(rnn_state)
    return results
# def loss(results):
#     losses=tf.nn.seq2seq2.sequence_loss_by_example()
pred=RNN(x)
cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=y))
train_op=tf.train.AdamOptimizer(0.001).minimize(cost)

correct_pred=tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(2000):
        batch=mnist.train.next_batch(batch_size)
        batch_x=batch[0]
        batch_y=batch[1]
        #print('1:',batch_x.shape)
        batch_x=batch_x.reshape([batch_size,n_steps,input_size])
        #print('2:', batch_x.shape)
        sess.run(train_op,feed_dict={x:batch_x,y:batch_y})
        if i % 100==0:
            print('step%d,trianing accuracy is %g'%(i,sess.run(accuracy,feed_dict={x:batch_x,y:batch_y})))
    test_len=int(mnist.test.num_examples/batch_size)+1
    test_count_all=0
    test_correct=0

    for i in range(test_len):
        test_batch=mnist.test.next_batch(batch_size)
        test_x=test_batch[0].reshape([batch_size,n_steps,input_size])
        test_correct+=accuracy.eval(feed_dict={x:test_x, y: test_batch[1]})
    print('test accuracy%g' % (test_correct/test_len))

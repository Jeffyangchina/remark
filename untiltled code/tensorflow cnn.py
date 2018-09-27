#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#@Author: Yang Xiaojun
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets('MNIST_data',one_hot=True)

#load data
x_data_test=mnist.test.images
y_data_test=mnist.test.labels
x_data_trian_Adm=mnist.train.images
y_data_trian_Adm=mnist.train.labels
in_size=784
out_size=10
#define placeholder
xs=tf.placeholder(tf.float32,[None,in_size])
ys=tf.placeholder(tf.float32,[None,out_size])
keep_prob=tf.placeholder(tf.float32)
#num_sample,28x28,num_channel
x_image=tf.reshape(xs,[-1,28,28,1])


def Weights(shape):
    w=tf.truncated_normal(shape,stddev=0.1,dtype=tf.float32)
    return tf.Variable(w)
def Biases(shape):
    bas=tf.constant(0.1,shape=shape,dtype=tf.float32)
    return tf.Variable(bas)
def conv2d(x,W):
    #must strides[1,x_move,y_move,1]
    conv1=tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')#VALID 全在图片里 ，SAME则在图片外以0填充
    return conv1
def maxpool(inx):
    #ksize is the pool patch size, strides is move step
    mp=tf.nn.max_pool(inx,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')#tf.nn.avg_pool()
    return mp
#define conv1 layer1
W_conv1=Weights([5,5,1,32])#5x5 is cnn patch size,1 is in size depth,32 is out size depth
b_conv1=Biases([32])
h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)#output size 28x28x32
out_con1=maxpool(h_conv1)#output size 14x14x32
#define conv2 layer2
W_conv2=Weights([5,5,32,64])
b_conv2=Biases([64])
h_conv2=tf.nn.relu(conv2d(out_con1,W_conv2)+b_conv2)#output size 7x7x64
out_con2=maxpool(h_conv2)#output size 7x7x64
#define function layer1
W_func1=Weights([7*7*64,1024])# insize,outsize
tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(0.0003)(W_func1))
b_func1=Biases([1024])#outsize
out_conv2_flat=tf.reshape(out_con2,[-1,7*7*64])#[n_sample,7,7,64]>>[n_sample,7*7*64]
out_func1=tf.nn.relu(tf.matmul(out_conv2_flat,W_func1)+b_func1)
out_drop=tf.nn.dropout(out_func1,keep_prob)
#define function layer2
W_func2=Weights([1024,10])# insize1024,outsize
tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(0.0003)(W_func2))
b_func2=Biases([10])#outsize
prediction=tf.nn.softmax(tf.matmul(out_drop,W_func2)+b_func2)

#loss between prediction and real data
with tf.name_scope('loss'):

    cross_entropy=-tf.reduce_sum(ys*tf.log(prediction))#adam适合这种
    tf.add_to_collection('losses',cross_entropy)
    losses=tf.add_n(tf.get_collection("losses"))
    #tf.summary.scalar('loss',cross_entropy)
#define train
#train_step=tf.train.GradientDescentOptimizer(0.1).minimize(losses)
train_step=tf.train.AdamOptimizer(1e-4).minimize(losses)#和GD差不多的准确率,大规模数据用adam
correct_predict=tf.equal(tf.argmax(prediction,1),tf.argmax(ys,1))#返回的是bool值
accuracy=tf.reduce_mean(tf.cast(correct_predict,'float'))
saver=tf.train.Saver()
#init
sess=tf.Session()
#merged=tf.summary.merge_all()#这是显示集合
#writer=tf.summary.FileWriter('logs/',sess.graph)#输出文件，用add
sess.run(tf.global_variables_initializer())
#train
with sess.as_default():
    for i in range(5000):#是比较慢的,每次迭代大约需0.6秒，最终达到0.98，普通神经网络的准确率（5000次迭代0.97）

        batch=mnist.train.next_batch(1)
        x_data_train =batch[0]
        y_data_train = batch[1]
        print('label:',y_data_train[0],type(y_data_train))
        #x_data_train =
        print('1:',y_data_train[0][5])
        #y_data_train =y_data_trian_Adm
        sess.run(train_step, feed_dict={xs: x_data_train, ys: y_data_train, keep_prob: 0.5})  # x_data,y_data为数据集

        if i%100==0:
            
            train_accuracy=accuracy.eval(feed_dict={xs:x_data_train,ys:y_data_train,keep_prob:1})
            print('step%d,trianing accuracy is %g'%(i,train_accuracy))
            #train_result =sess.run(merged,feed_dict={xs:x_data_train,ys:y_data_train,keep_prob:1})
            #test_result = sess.run(merged, feed_dict={xs: x_data_test, ys: y_data_test,keep_prob:1})
            #writer.add_summary(train_result,i)
            #writer.add_summary(test_result, i)
    print('finished')
    save_path = saver.save(sess, 'yangcnn/tensor.ckpt')
    test_len = int(mnist.test.num_examples / 50) + 1
    test_count_all = 0
    test_correct = 0

    for i in range(test_len):
        test_batch = mnist.test.next_batch(50)
        test_x = test_batch[0]
        test_y = test_batch[1]
        test_correct += accuracy.eval(feed_dict={xs: test_x, ys: test_y,keep_prob:1})
        test_count_all+=1
    print('test accuracy%g' % (test_correct / test_len))
    print(test_count_all,test_len)




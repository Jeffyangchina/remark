#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers
from text_cnn import TextCNN
from tensorflow.contrib import learn
import csv
from sklearn.preprocessing import OneHotEncoder
path_db='./cnn-text-classification-tf-master/Db_classify.db'
# Parameters
# ==================================================

# Data Parameters
tf.flags.DEFINE_string("positive_data_file", "./data/rt-polaritydata/rt-polarity.pos", "Data source for the positive data.")
tf.flags.DEFINE_string("negative_data_file", "./data/rt-polaritydata/rt-polarity.neg", "Data source for the negative data.")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./cnn-text-classification-tf-master/run/checkpoints/", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", True, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")

# CHANGE THIS: Load data. Load your own data here
# if FLAGS.eval_train:
#     x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.positive_data_file, FLAGS.negative_data_file)
#     y_test = np.argmax(y_test, axis=1)
# else:
#     x_raw = ["a masterpiece four years in the making", "everything is off."]
#     y_test = [1, 0]
def get_fr_csv(path):
    import csv
    csvFile = open(path, "r", encoding='UTF-8')
    reader = csv.reader(csvFile)
    data_out=[]
    for item in reader:
        if item:
            data_out.append(item)
    return data_out
def load_data(path):
    train_data = get_fr_csv(path)
    tr_x_= [x[:-1] for x in train_data]#这是一个数组中数组
    tr_y_ = [[x[-1]] for x in train_data]#但这是个数组中字符串
    ohe = OneHotEncoder()
    ohe.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
    tr_y = ohe.transform(tr_y_).toarray()
    tr_x=[]
    for x in tr_x_:
        tr_x+=x
    return tr_x,tr_y
# Map data into vocabulary
# csv_path='./T01.csv'
# x_raw,y_test=load_data(csv_path)
# y_test = np.argmax(y_test, axis=1)
parent_p = os.path.dirname(FLAGS.checkpoint_dir)
parent_path = os.path.dirname(parent_p)
print("add file0: {}".format(parent_path))
vocab_path = os.path.join(parent_path, "vocab")
#vocab_path = os.path.join("..", FLAGS.checkpoint_dir, "vocab")
vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
# x_test = np.array(list(vocab_processor.transform(x_raw)))

print("\nEvaluating...\n")
def singal_test(x_raw,predictions):
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
            allow_soft_placement=True,
            log_device_placement=False)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            saver = tf.train.import_meta_graph("{}.meta".format(meta_graph))
            saver.restore(sess, checkpoint_file)
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]
            x_test = np.array(list(vocab_processor.transform(x_raw)))
            predict_out= sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            return predict_out
# Evaluation
# ==================================================
checkpoint_file = r'./cnn-text-classification-tf-master/run/checkpoints/model-79200'
meta_graph=r'./cnn-text-classification-tf-master/run/checkpoints/model-79200'
# checkpoint_file = tf.train.NewCheckpointReader(checkpoint_file)
# checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
print("add file: {}".format(checkpoint_file))
graph = tf.Graph()
with graph.as_default():
    session_conf = tf.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # Load the saved meta graph and restore variables
        # saver = tf.train.import_meta_graph(meta_graph)
        saver = tf.train.import_meta_graph("{}.meta".format(meta_graph))
        # saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))

        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        print('0:',type(input_x))
        # input_y = graph.get_operation_by_name("input_y").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

        # Tensors we want to evaluate
        predictions = graph.get_operation_by_name("output/predictions").outputs[0]

        rootdir=r'./cnn-text-classification-tf-master/for test data set'
        lists = os.listdir(rootdir)
        for i in range(0, len(lists)):
            path = os.path.join(rootdir, lists[i])

            if os.path.isfile(path):
                x_raw, y_test = load_data(path)
                y_test = np.argmax(y_test, axis=1)
                x_test = np.array(list(vocab_processor.transform(x_raw)))
        # Generate batches for one epoch
                batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

        # Collect the predictions here
                all_predictions = []

                for x_test_batch in batches:
                    batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                    all_predictions = np.concatenate([all_predictions, batch_predictions])

# Print accuracy if y_test is defined
                if y_test is not None:
                    correct_predictions = float(sum(all_predictions == y_test))
                    print("Total number of test examples: {}".format(len(y_test)))
                    print("Accuracy: {:g}".format(correct_predictions/float(len(y_test))))

# Save the evaluation to a csv
                predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
                out_path = os.path.join(FLAGS.checkpoint_dir, "..", "prediction_"+lists[i])
                print("Saving evaluation to {0}".format(out_path))
                with open(out_path, 'w') as f:
                    csv.writer(f).writerows(predictions_human_readable)

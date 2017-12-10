import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
sess = tf.Session()

from keras import backend as K
K.set_session(sess)
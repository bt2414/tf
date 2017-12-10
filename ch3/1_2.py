import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable("v", shape=[1], initializer=tf.zeros_initializer)

g2 = tf.Graph()
with g2.as_default():
    v = tf.get_variable("v", shape=[1], initializer=tf.ones_initializer)

with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        print(sess.run(tf.get_variable("v")))

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")

result = a + b

print result
print tf.Session().run(result)

config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)

sess1 = tf.InteractiveSession(config=config)
sess2 = tf.Session(config=config)

print sess1
print sess2
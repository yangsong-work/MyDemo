import tensorflow as tf
import  numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

#4.5.1
# with tf.variable_scope("foo") as scope:
#     v = tf.get_variable("v", [1])
#     print(v)
# with tf.variable_scope("foo", reuse=True):
# #也可以写成：
# #scope.reuse_variables()
#     v1 = tf.get_variable("v", [1])
# assert v1 == v

# with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
#     v = tf.get_variable("v", [1])
#     assert v.eval() == 0.4
#     # w = tf.get_variable("w", [1], initializer=tf.constant_initializer(0.3)):
#     # assert w.eval() == 0.3 # 重写初始化器的值
#
#     # with tf.variable_scope("bar"):
#     #   v = tf.get_variable("v", [1])
#     #   assert v.eval() == 0.4 # 继承默认的初始化器
#     # with tf.variable_scope("baz", initializer=tf.constant_initializer(0.2)):
#     #      v = tf.get_variable("v", [1])
#     #      assert v.eval() == 0.2 # 重写父作用域的初始化器的值

# with tf.variable_scope("foo"):
#   x = 1.0 + tf.get_variable("v", [1])
#   print(x.op.name)
#   assert x.op.name == "foo/add"


#4.5.2
# if __name__ == '__main__':
# with tf.variable_scope("foo"):
#     with tf.name_scope("bar"):
#         v = tf.get_variable("v", [1])
#         b = tf.Variable(tf.zeros([1]), name='b')
#         x = 1.0 + v
# print (v.name == "foo/v:0")
# assert b.name == "foo/bar/b:0"
# assert x.op.name == "foo/bar/add"

#4.6 批标准化
# 计算Wx_plus_b的均值和方差，其中axes=[0]表示想要标准化的维度
# fc_mean, fc_var = tf.nn.moments(Wx_plus_b, axes=[0], )
# scale = tf.Variable(tf.ones([out_size]))
# shift = tf.Variable(tf.zeros([out_size]))
# epsilon = 0.001
# Wx_plus_b = tf.nn.batch_normalization(Wx_plus_b, fc_mean, fc_var, shift,
# scale, epsilon)
# 也就是在做：
# Wx_plus_b = (Wx_plus_b - fc_mean) / tf.sqrt(fc_var + 0.001)
# Wx_plus_b = Wx_plus_b * scale + shift




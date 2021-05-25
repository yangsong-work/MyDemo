
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

#sigmoid函数
a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
sess = tf.Session()
print (sess.run(tf.sigmoid(a)))

#relu函数
a = tf.constant([-1.0, 2.0])
with tf.Session() as sess:
    b = tf.nn.relu(a)
    print (sess.run(b))

#dropout函数
a = tf.constant([[-1.0, 2.0, 3.0, 4.0]])
with tf.Session() as sess:
    b = tf.nn.dropout(a, 0.5, noise_shape = [1,4])
    print (sess.run(b))
    b = tf.nn.dropout(a, 0.5, noise_shape = [1,1])
    print (sess.run(b))

#当输入数据特征相差明显时，用tanh的效果会很好，且在循环过程中会不断扩大特征效果并显示出
#来。当特征相差不明显时，sigmoid效果比较好。同时，用sigmoid和tanh作为激活函数时，需要对输入进行规
#范化，否则激活后的值全部都进入平坦区，隐层的输出会全部趋同，丧失原有的特征表达。而relu会好很
#多，有时可以不需要输入规范化来避免上述情况。
#因此，现在大部分的卷积神经网络都采用relu作为激活函数。我估计大概有85%～90%的神经网络会
#采用ReLU，10%～15%的神经网络会采用tanh，尤其用在自然语言处理上。

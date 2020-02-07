import tensorflow as tf

'''例子1 对一维数组改变维度'''
# a=tf.Variable([1,2,3,4])
# print("a.shape:",a.shape)
# print("a:",a)
# print("-"*50)
# a2 = a[tf.newaxis, :]
# print("a2.shape:",a2.shape)
# print("a2:",a2)
# print("-"*50)
# a3 = a[:,tf.newaxis]
# print("a3.shape:",a3.shape)
# print("a3:",a3)

# print('='*50)

'''例子2 对二维数组改变维度'''
# 在原有的2个维度中间插入一个维度
b=tf.constant([[1,2,3],[4,5,6]])
print("b.shape:",b.shape)
print("b:",b)
print("-"*50)
b2 = b[:,tf.newaxis]
print("b2.shape:",b2.shape)
print("b2:",b2)

print('='*50)

# 在原有的维度后增加一个维度
b=tf.constant([[1,2,3],[4,5,6]])
print("b.shape:",b.shape)
print("b:",b)
print("-"*50)
b3 = b[:,:,tf.newaxis]
print("b3.shape:",b3.shape)
print("b3:",b3)
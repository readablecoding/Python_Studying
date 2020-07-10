# -*- coding: utf-8 -*-
"""2_TensorFlow_DataType.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1488L9zDCwMypQ42F2C9s3a4pbAYpk6JG

# **TensorFlow 자료형**
- 상수(constant) : 미리 정해진 값, 불변형의 자료형이므로 수정 불가
- 변수(Variable) : 값을 바꿀 수 있는 자료형, 미분이나 최적화할 때 사용
"""

import tensorflow as tf
tf.__version__

"""## 1)TensorFlow constant 만들기"""

tf.constant([1, 2, 3])

tf.constant([[1, 2, 3], [4, 5, 6]])

tf.range(10)

tf.linspace(0.0, 5, 11) # start 값은 부동소수점으로 주어져야 함

"""- tf.zeros(shape)
- tf.zeros_like(tensor)
- tf.ones(shape)
- tf.ones_like(tensor)
- tf.fill(shape, value)
"""

tf.zeros((2, 3))

tf.ones([2, 3])

tf.fill([4, 5], 5)

a = tf.ones_like([[1, 2], [4, 5]])

a

"""# **난수 텐서 만들기**
- tf.random.set_seed(seed) # 씨앗값 설정
- tf.random.uniform() # 균등분포
- tf.random.normal() #  정규분포
- tf.random.shuffle() # 섞기
"""

tf.random.set_seed(0)

tf.random.uniform((2, 3), seed = 0)

tf.random.uniform((2, 3), seed = 0)

"""# **Tensor 중요 속성(Numpy와 동일)**
- ndim
- shape
- dtype
"""

a = tf.range(5, dtype = tf.float32)
a

print("차원 : ", a.ndim)
print("쉐이프 : ", a.shape)
print("데이터 타입 : ", a.dtype)

a

a.numpy()

"""# **차원의 변화**
- tf.reshape
- tf.transpose
"""

a = tf.range(6, dtype = tf.float32)
a

a_re = tf.reshape(a, (2, 3))
a_re

a

a_tp = tf.transpose(a_re)
a_tp

"""# **실수 변수형 텐서의 생성**"""

s = tf.Variable(1.0)
s

v = tf.Variable(tf.ones((2, )))
v

x = tf.Variable(tf.ones((2, 3)))
x

"""# **변수의 값 바꾸기**
- x.assign(tf.zeros((2, 3)))
- x.assign_add() : 값을 증가, 자바의 += 과 유사
- x.assign_sub() : 값을 감소, 자바의 -= 과 유사
"""

x.assign(tf.zeros((2, 3)))

a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3]) 
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2]) 
c = tf.matmul(a, b) 

c

"""# **미분**"""

x = tf.Variable(tf.constant(1.0))
x



# tf.matmul() != tf.multiply()

y = tf.constant(5)
with tf.GradientTape() as tape:
  y = tf.multiply(5, x)

gra = tape.gradient(y, x)
gra.numpy()

x1 = tf.Variable(tf.constant(1.0))
x2 = tf.Variable(tf.constant(1.0))

with tf.GradientTape() as tape:
  y = tf.multiply(x1, x2)

gra = tape.gradient(y, [x1, x2])
gra

gra[0].numpy()
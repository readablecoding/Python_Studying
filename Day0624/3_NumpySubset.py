#!/usr/bin/env python
# coding: utf-8

# ## Numpy Indexing, Slicing
# - ndarray로부터 특정 요소를 가져오는 방법

# In[7]:


import numpy as np


# In[11]:


ary = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(ary)
print(ary[0][0])


# In[13]:


a = np.array(ary)
print(a)
print(a[0, 0]) #a의 0행 0열


# In[16]:


a[0, 0] = 12 
print(a)
print()
a[0, 0] = 55
print(a)


# ### Boolean Indexing
# - 배열의 각 요소의 값을 검사해서 그 여부가 True 인지 False인지 지정하는 방식
# - 특정 조건에 따라서 배열의 형태로 추출 가능

# In[26]:


import numpy as np


# In[27]:


a = np.arange(1, 25).reshape(4, 6)
print(a)


# In[28]:


even_ary = a % 2 == 0 #짝수인지 확인
print(even_ary)


# In[29]:


a = a[a % 2 == 0]
print(a)


# In[34]:


a = np.arange(1, 25).reshape(4, 6)
a = a[a % 2 != 0]
print(a)


# In[35]:


a = np.arange(1, 25).reshape(4, 6)
a = a[even_ary]
print(a)


# In[1]:


# comparison을 이용한 추출


# In[2]:


import numpy as np


# In[4]:


a = np.array([1, 4, 5, 2, 0, 3, 8, 9, 7, 6], float)
print(a)


# In[7]:


print(a > 4)
print(a[a > 4])


# In[8]:


b = a[a > 4]
print(b)


# ### Fancy Indexing
# - 배열에 인덱스 배열을 전달해서 요소를 추출하는 방법
# - 인덱스 value를 이용해서 값을 추출하는 방법

# In[9]:


import numpy as np


# In[23]:


a = np.arange(1, 25).reshape(4, 6)


# In[24]:


print(a[0, 0], a[1, 1], a[2, 2]) #0행 0열, 1행 1열, 2행 2열의 값 출력


# In[25]:


b = [a[0, 0], a[1, 1], a[2, 2]] #fancy indexing
print(b)


# In[26]:


print(a)


# In[29]:


#행과 열의 인덱스 키 값으로 쓰는 것이 fancyindexing이다, 정해진 배열의 크기를 준수해야 한다
index1 = np.array([0, 0, 1, 1, 0]) #행의 역할을 하게 됨
index2 = np.array([1, 1, 0, 5, 1]) #열의 역할을 하게 됨
print(a[index1, index2])


# In[5]:


d = np.array([[10, 11], [12, 13]], float) #float를 통해 소수점을 가지게 된다
print(d)


# In[6]:


print(d[index1]) #index1이 행을 추출하는 역할, 열을 표기 안해서 행의 데이터만 가져 온다

#index1이 열의 역할을 하게 하고 싶다.
print(d[0, index1])


# ## Slicing
# - Ndarray에서 특정 요소를 추출하는 것
# - 행과 열을 나눠서 추출 가능
# - Matrix에서 부분집합을 추출할 때 매우 유용: 0차원(벡터), 1차원(Array), 2차원(Matrix), 3차원 이상(tensor)

# In[40]:


import numpy as np


# In[42]:


origin = np.arange(1, 25).reshape(4, 6)
print(origin)


# In[43]:


print(origin[1:3, 1:5]) #행은 1~2행, 열은 1~4행까지


# In[45]:


#음수 인덱스의 사용
print(origin[1:-1, 1:-1]) #1행부터 마지막 행 전까지, 1열부터 마지막 열 전까지


# In[46]:


print(origin)


# In[48]:


target = origin[1:3, 1:5]
print(target)


# In[49]:


print(target[:, 1:3])


# In[53]:


target[:, 1:3] = 999 #스칼라 값을 대입하니 배열의 값이 바뀜
print(target)


# In[57]:


print(origin) #target은 origin의 데이터의 일부를 보여주는 일종의 창 역할 수행-> 원본 데이터를 참조하고 있으므로 원본 데이터도 변화함


# ## 배열의 연산
# - 기본 연산자를 재정의 해서 직관적으로 표현

# In[65]:


# +, add()
# -, subtract()
# /, divide()
# *, multiply()
# exp() -> 지수 구하기
# sqrt() -> 루트 값
# sin()
# cos()
# tan()
# log()

#matrix 곱: dot()


# In[2]:


import numpy as np


# In[3]:


a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(3, 2)
print(a)
print()
print(b)


# In[71]:


print(np.dot(a, b)) #매트릭스 곱 구하기


# In[72]:


print(a.dot(b)) #매트릭스 곱 구하기


# In[76]:


#전치 행렬 만들기
c = np.random.randint(1, 10, (2, 3)) #1에서 9까지 수 중에서 난수를 발생해 2행 3열로 표현


# In[77]:


print(c)


# In[78]:


print(c.T) #전치 행렬 만드는 방법: 객체.T로 표현한다


# In[79]:


#
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(9, 0, -1).reshape(3, 3)
print(a)
print()
print(b)


# In[80]:


print(a > b) 


# In[81]:


print(a < b)


# In[82]:


print(a == b)


# In[85]:


print(np.array_equal(a, a))


# In[87]:


print(np.array_equal(a, b))


# ## aggregation 

# In[90]:


# sum()
# min(), max()
# mean()
# argmax(), argmin()


# In[91]:


import numpy as np


# In[92]:


a = np.arange(1, 21)
print(a)


# In[94]:


np.random.shuffle(a)
print(a)


# In[96]:


a = a.reshape(4, 5)
print(a)


# In[102]:


print(np.argmax(a)) #가장 큰 값인 20이 위치한 곳을 찾기 위해 열 방향으로 가면서 0부터 시작해 진행


# In[103]:


print(np.argmax(a, axis=0)) #열 중에서 가장 큰 값이 있는 곳의 행의 값을 보여줌


# In[104]:


print(np.argmax(a, axis=1)) #열의 값을 보여줌


# In[ ]:





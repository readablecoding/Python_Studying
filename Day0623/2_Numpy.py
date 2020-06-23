#!/usr/bin/env python
# coding: utf-8

# ### <font color="orange">Numpy로 구현하는 다차원 배열</font>
# 
# - **Numpy** 를 사용하면 <span style="color:red; background: yellow">다차원 배열</span>을 효율적으로 다룰 수 있다
# - `import numpy as np` 형태로 import해서 사용 함 #숫자 1번 옆에 있는 것을 누르면 ''를 통해 색이 칠해진 영역이 생김

# In[2]:


import numpy as np


# In[5]:


nestedmlist = [[11, 12, 13], [21, 22, 23], [31, 32, 33]] # 3행 3열의 파이썬 리스트
mathNdarray = np.array(nestedmlist)
print(mathNdarray)


# In[6]:


# 각 원소에 1을 증가(Broadcasting 기능)
mathNdarray = mathNdarray + 1
print(mathNdarray)


# ### numpy에서 제공하는 수치계산용 메소드의 사용

# In[35]:


# 3행(1축) 3열(0축)의 파이썬 리스트
nestedmlist = [[11, 12, 13], [21, 22, 23], [31, 32, 33]] # 3행 3열의 파이썬 리스트
mathNdarray = np.array(nestedmlist)

# 전체 합
print("전체 합 :", np.sum(mathNdarray))
print("축 0 합 :", np.sum(mathNdarray, axis=0))
print("축 1 합 :", np.sum(mathNdarray, axis=1))


# In[36]:


# 전체 평균
print("전체 평균 :", np.mean(mathNdarray))
print("축 0 평균 :", np.mean(mathNdarray, axis=0))
print("축 1 평균 :", np.mean(mathNdarray, axis=1))


# In[37]:


# 최솟값
print("최솟값 :", np.amin(mathNdarray))
print("축 0 최솟값 :", np.sum(mathNdarray, axis=0))
print("축 1 최솟값 :", np.sum(mathNdarray, axis=1))


# In[38]:


# 최댓값
print("최댓값 :", np.amax(mathNdarray))
print("축 0 최댓값 :", np.amax(mathNdarray, axis=0))
print("축 1 최댓값 :", np.amax(mathNdarray, axis=1))


# In[39]:


# 중앙값
print("중앙값 :", np.median(mathNdarray))
print("축 0 중앙값 :", np.sum(mathNdarray, axis=0))
print("축 1 중앙값 :", np.sum(mathNdarray, axis=1))


# In[40]:


# 분산
print("분산 :", np.var(mathNdarray))
print("축 0 분산 :", np.var(mathNdarray, axis=0))
print("축 1 분산 :", np.var(mathNdarray, axis=1))


# In[41]:


# 표준편차
print("표준편차 :", np.std(mathNdarray))
print("축 0 표준편차 :", np.std(mathNdarray, axis=0))
print("축 1 표준편차 :", np.std(mathNdarray, axis=1))


# ### ndarray 생성하는 여러가지 방법에 대한 이해

# In[47]:


import numpy as np


# In[49]:


# list를 이용해서 만드는 방법
a = np.array([1,2,3])
print(a)


# In[52]:


# np.arange()
a = np.arange(1, 11)
print(a)
print()
a = np.arange(1, 11, 0.5)
print(a)


# In[54]:


# zeros, ones, full, identity
a = np.zeros((3, 4), dtype=np.int16)
print(a)


# In[59]:


a = np.ones((2, 3, 4), dtype=np.int16) #2개의 면, 3개의 행, 4개의 열
print(a)


# In[60]:


a = np.full((5, 5), 7, dtype=np.float32) #5행 5열, 숫자 7로 채우기, 32비트 타입 데이터
print(a)


# In[65]:


a = np.empty((4, 2), dtype=np.int32) #초기화하지 않겠다 !!
print(a)


# In[71]:


b = np.ones_like(a) #배열의 크기만큼을 1로 채우겠다, zeros_like, full_like, empty_like
print(b)


# In[68]:


c = np.zeros_like(a) #배열의 크기만큼 0으로 채우겠다
print(c)


# In[70]:


b = np.eye(5) #단위 행렬을 만드는 eye(), 행렬계의 1과 같은 것( 23 * 1 = 23 )
print(b)


# ## Numpy dtype의 종류
# - bool (True, False)
# - **`int (int8, int16, int32, int64, int128)`**
# - uint (uint8, uint16, uint32, uint64, uint128) #부호 없는 정수
# - **`float (float32, float64)`**
# - complex(complex64, complex128) #복소수
# - str, unicode
# - object

# ### ndArray의 속성들
# - shape : numpy array의 dimension을 튜플의 형태로 전환 (4, ) (1, 4)
# - dtype : numpy array의 dtype을 반환
# - ndim :  numpy array의 차수 리턴
# - size :  numpy array의 요소 개수
# - nbytes:  numpy array의 메모리 크기 반환

# ### ndarray의 중요한 메서드들
# - len(배열명): 배열의 요소 개수 리턴
# - astype(): 배열의 타입 변환
# - **`reshape(): 배열의 shape을 수정 `**
# - flatten(): 다차원의 배열을 1차원으로 수정

# In[91]:


a = [[1, 2, 3], [5, 6, 7]]
b = np.array(a)
print(b)
print("len() :", len(b), ", len(lenb[0]) :", len(b[0]))


# In[79]:


b = b.astype(np.float)
print(b)


# In[85]:


a = np.arange(24)
print(a)
print()
b = a.reshape(4, 6)
print(b)
print()
c = b.flatten()
print(c)


# In[90]:


import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0, 10, 2, np.float)
print(a)

plt.plot(a, 'o')
plt.show()


# ### 난수 발생
# - 난수란 특정 시작 숫자로부터 난수처럼 보이는 수열을 만드는 알고리즘의 결과물
# - np.random.seed(100)

# In[92]:


import numpy as np
a = np.random.random((3, 3)) #3행 3열, 1을 초과하지 않는 실수로 표현
print(a)


# In[97]:


b = np.random.randint(0, 10, (2, 3)) #0부터 9까지 발생, 2행 3열의 데이터로 담음
print(b)


# In[100]:


np.random.seed(100)
a = np.random.random((3, 3))
print(a)

print()

b = np.random.randint(0, 10, (2, 3)) #0부터 9까지 발생, 2행 3열의 데이터로 담음
print(b)


# In[101]:


# 정규분포에 해당하는 난수 발생하기

mean = 0
std = 1

a = np.random.normal(loc= mean, scale=std, size=(2, 3)) #loc는 평균, scale은 표준편차
print(a)


# In[105]:


data = np.random.normal(0, 1, 10000)

plt.hist(data, bins=100)
plt.show()


# In[106]:


# 균등분포
data = np.random.rand(10000)
plt.hist(data, bins=10)
plt.show()


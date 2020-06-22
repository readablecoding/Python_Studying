#!/usr/bin/env python
# coding: utf-8

# ## Numpy 기초
# - numpy를 사용 : 데이터 사이언스에서 사용하는 중요한 패키지<br> => 행렬(선형대수)
# - numpy 다음에는 <b style="color:red">pandas</b>를 배워서 데이터 전처리 작업을 한다 
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/330px-NumPy_logo.svg.png">

# In[4]:


import numpy as np


# ## 1. 숫자 자료 처리하기(기초)

# In[5]:


math1 = 89
math2 = 95
math3 = 75


# In[6]:


m_sum = math1 + math2 + math3
m_avg = m_sum / 3 


# In[9]:


print("수학 점수의 합계: {}".format(m_sum))
print("수학 점수의 평균: {}".format(m_avg))


# In[10]:


math4 = 87


# In[11]:


m_sum = math1 + math2 + math3 + math4
m_avg = m_sum / 4 


# In[12]:


print("수학 점수의 합계: {}".format(m_sum))
print("수학 점수의 평균: {}".format(m_avg))


# ## 2.리스트 자료형으로 처리

# In[23]:


mlist = [89, 95, 75]
print(mlist)


# In[24]:


m_sum1 = 0
m_avg1 = 0


# In[25]:


# for문을 이용해서 합계 평균 구하기
for e in mlist :
    m_sum1 += e

m_avg1 = m_sum1 / len(mlist)
    
print("수학 점수의 합계: {}".format(m_sum1))
print("수학 점수의 평균: {}".format(m_avg1))


# In[26]:


mlist.append(87)
print(mlist)


# In[28]:


m_sum1 = 0
m_avg1 = 0


# In[29]:


# for문을 이용해서 합계 평균 구하기
for e in mlist :
    m_sum1 += e

m_avg1 = m_sum1 / len(mlist)
    
print("수학 점수의 합계: {}".format(m_sum1))
print("수학 점수의 평균: {}".format(m_avg1))


# ### 3)문제 발생: 채점에 문제가 생겨 모든 학생의 점수를 모두 1점씩 올려줘야 하는 일이 발생

# In[3]:


mlist = [89, 95, 75, 87]

m_sum1 = 0
m_avg1 = 0
# for문을 이용해서 합계 평균 구하기
for e in mlist :
    m_sum1 += e

m_avg1 = m_sum1 / len(mlist)
    
print("수학 점수의 합계: {}".format(m_sum1))
print("수학 점수의 평균: {}".format(m_avg1))


# In[5]:


##문제 해결 -> 1점 더하기
mlist_new = [e + 1 for e in mlist]
print(mlist_new)


# In[6]:


# for문을 이용해서 합계 평균 구하기
m_sum2 = 0
m_avg2 = 0

for e in mlist_new :
    m_sum2 += e

m_avg2 = m_sum2 / len(mlist_new)
    
print("수학 점수의 합계: {}".format(m_sum2))
print("수학 점수의 평균: {}".format(m_avg2))


# ### 4) 학생 수의 증가로 3반으로 증가했다고 가정 ==> 한 반에 4명씩 3반이 생겼다
# 

# In[22]:


#1반: 10, 20, 30, 40
#2반: 21, 22, 23, 24
#3반: 31, 32, 33, 34


# In[29]:


nested_mlist = [[10, 20, 30, 40], [21, 22, 23, 24], [31, 32, 33, 34]]
print(nested_mlist)


# In[34]:


#문제 해결(Python으로 해결)
nested_mlist_new = []
for tmp in nested_mlist:
    tList = []
    for e in tmp:
        tList.append(e+1)
    nested_mlist_new.append(tList)

print(nested_mlist_new)


# In[42]:


#Python으로 해결 하기
nested_mlist = [[10, 20, 30, 40], [21, 22, 23, 24], [31, 32, 33, 34]]
print(nested_mlist)


#mlist_new = [e + 1 for e in mlist]
#print(mlist_new)


# In[98]:


### Numpy로 해결 하기
import numpy as np

nested_mlist = [[10, 20, 30, 40], [21, 22, 23, 24], [31, 32, 33, 34]]
print(nested_mlist)
print()
tmp = np.array(nested_mlist)
print("**1점 증가 전 : \n{}".format(tmp))
print()
tmp = tmp + 1 #브로드캐스팅 작업
print("**1점 증가 후: \n{}".format(tmp))


# ### Numpy 패키지로 해결하기
# 
# - 파이썬으로 만든 수치계산 패키지
# - 데이터 분석 패키지
# - 내부는 C로 만들어져 있어서 계산 속도가 엄청 빠르다
# - Array 형태의 데이터 처리: 선형대수학

# In[45]:


l = [1, 1,5, "hong", [1, 2, 3, 4]] #파이썬 리스트
print(l)


# In[47]:


import numpy as np  #파이썬 배열을 이용해서 numpy 배열을 만든다


# In[50]:


print(np.__version__)


# In[64]:


# 단일 값 : 스칼라
a = np.array(10) #a는 스칼라 값
print(a)
print(a.dtype) #타입, type(a) -> 10
print(a.ndim) #차원 -> int32
print(a.shape) #몇 행 몇 열인가? -> (), 행렬이 아니어서
print(a.nbytes) # 바이트 수 -> 4
print(a.size) # 요소 개수 -> 1


# In[66]:


# 1차원 배열
b = np.array([1, 2, 3, 4, 5])
print(b)  #[1 2 3 4] -> 콤마가 안 찍힘
print(b.dtype) #타입, type(a) 
print(b.ndim) #차원 
print(b.shape) #몇 행 몇 열인가? 
print(b.nbytes) # 바이트 수 
print(b.size) # 요소 개수 


# In[67]:


#2차원 배열 (3 x 2)
c = np.array([[1, 2], [4, 5], [7, 8]])
print(c)
print(c.dtype) #타입, type(b) 
print(c.ndim) #차원 
print(c.shape) #몇 행 몇 열인가? 
print(c.nbytes) # 바이트 수 
print(c.size) # 요소 개수 


# In[68]:


#3차원 배열 (2면 x 2행 x 3열)
d = np.array([[[1, 2, 3], [3, 4, 5]], [[11, 22, 33], [32, 42, 52]]])
print(d)
print(d.dtype) #타입, type(d) 
print(d.ndim) #차원 
print(d.shape) #몇 행 몇 열인가? 
print(d.nbytes) # 바이트 수 
print(d.size) # 요소 개수 


# In[72]:


# numpy는 배열에 다른 타입의 데이터를 허용하지 않는다.
test_ary = np.array([1, 4, "5", "8"], dtype = np.float)
print(test_ary)
print(test_ary.dtype) #타입, type(test_ary) 
print(test_ary.ndim) #차원 
print(test_ary.shape) #몇 행 몇 열인가? 
print(test_ary.nbytes) # 바이트 수 
print(test_ary.size) # 요소 개수 


# In[74]:


a = np.arange(1, 101, 2) #숫자 발생 (1부터 2씩 증가해 100까지)
print(a)


# In[82]:


a = np.arange(1, 11, 0.5) #1차원의 배열을 생성(시작 값, 끝 값(제외되는 값), 증가값)
print(a)
print("개수 : ", a.size)


# In[88]:


a = np.arange(1, 11, 0.5) #1차원의 배열을 생성(20개)

a = a.reshape(10, 2) #2차원 배열을 생성, 10행, 2열 -> 개수 만큼을 활용해 reshape이 가능하다
print(a)


# In[89]:


a = a.reshape(5, 4)
print(a)


# ## Numpy의 broadcasting
# - 개념: 차원이 다른 배열들 간의 연산을 하려고 할 때 특정 조건이 만족이 되면 연산이 되도록 자동으로 변환하는 것

# In[92]:


tmp = np.arange(1, 10).reshape(3, 3)
print(tmp + 1)


# ## Numpy 주요 연산 함수 

# In[102]:


import numpy as np
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(9, 0, -1).reshape(3, 3)
print(a) # 3행 3열: 축이 2개 (0축, 1축) 끝에 있는 것이 0축, 앞에 있는 것이 1축
print()
print(b)


# In[106]:


print(a.sum())
print(np.sum(a))


# ## 축(axis)의 개념
# 
# 

# In[109]:


print(a.sum(axis=0)) #0축, 세로로 값을 더함


# In[110]:


print(a.sum(axis=1)) #1축, 가로로 값을 더함


# In[118]:


b = np.array([[[1, 2, 3], [3, 4, 5]], [[11, 22, 33], [32, 42, 52]]]) #2 x 2 x 3  (2축, 1축, 0축)
print(b)


# In[122]:


print(b.sum(axis=0)) #0축, 열이 같은 것끼리 더하기


# In[123]:


print(b.sum(axis=1)) #1축, 행이 같은 것끼리 더하기


# In[124]:


print(b.sum(axis=2)) #2축, 면이 같은 것끼리 더하기


# In[ ]:





# In[ ]:





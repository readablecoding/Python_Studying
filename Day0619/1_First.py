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


# In[ ]:





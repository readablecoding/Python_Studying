#!/usr/bin/env python
# coding: utf-8

# ## [연습] Boolean Indexing 응용해보기
# - csv 파일은 xlsx보다 용량이 1/ 10 정도

# In[2]:


import numpy as np
import pandas as pd
import os


# In[3]:


print(os.getcwd())


# In[4]:


ris = pd.read_csv('./data/Seattle2014.csv')


# In[15]:


ris # DataFrame


# In[18]:


ris.head() #앞의 데이터 5개만 보여줌


# In[17]:


ris.tail() #뒤의 5개 데이터만 보여줌


# In[21]:


arr = ris['PRCP'].values #제목이 PRCP인 것의 데이터만 추출
arr


# In[24]:


days = np.arange(0, 365) 
ja = days < 31 #1월에 대한 조건 생성


# In[27]:


january = arr[ja] #1월 강수량 데이터 추출
print(january)


# In[79]:


#문제-1 : 비가 40 미만으로 내린 날이 몇 일인가?
data = january[january < 40]
print(data.size)


# In[ ]:


#문제-2 : 1월에 내린 강수량의 합, 평균강수량


# In[41]:


print(np.sum(january))
print(np.mean(january))


# In[ ]:


#문제-3 : 2월에 비는 몇 일이나 내렸나?


# In[88]:


fa = np.logical_and(days >= 31, days < 59) #전체 자료 중 해당 기간 자료 추출
febuary = arr[fa] 
print(febuary)
data2 = febuary[febuary > 0]
print(data2.size)


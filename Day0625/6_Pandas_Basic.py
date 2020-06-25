#!/usr/bin/env python
# coding: utf-8

# ## Pandas 개요
# - Structured된 데이터의 처리를 지원하는 파이썬 라이브러리
# - Numpy와 결합해서 스프레드시트를 처리하는 기능을 제공
# - Indexging, 연산함수, 결측치를 처리하는 전처리 기능 제공

# ### <span style="color:blue">1) Pandas 구성 요소 확인</span>
# - Dataframe: Data Table 전체를 의미하는 용어
# - Series: DataFrame 중에서 하나의 column에 해당하는 데이터 -> 세로의 데이터
# 
# #### Series

# In[3]:


from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[5]:


list_data = [1, 2, 3, 4, 5]


# In[8]:


p_sample = Series(data = list_data) #데이터를 가지고 시리즈를 만드는데 시리즈는 인덱스와 값으로 나타낸다


# In[10]:


print(p_sample) #인덱스를 기준으로 데이터를 붙이기도 한다. 기본적으로 인덱스는 0부터 시작한다


# In[11]:


#index를 특별히 지정하지 않으면 0부터 시작
#index를 문자로 해도 됨


# In[15]:


list_data = [1, 2, 3, 4, 5]
list_name = ['a', 'b', 'c', 'd', 'e']
obj = Series(data = list_data, index = list_name)
print(obj)


# In[ ]:





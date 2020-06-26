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

# In[1]:


from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[2]:


list_data = [1, 2, 3, 4, 5] #파이썬 리스트를 이용해서 데이터 준비. csv로 read_csv()를 더 많이 쓴다


# In[3]:


p_sample = Series(data = list_data) #데이터를 가지고 시리즈를 만드는데 시리즈는 인덱스와 값으로 나타낸다


# In[4]:


print(p_sample) #인덱스를 기준으로 데이터를 붙이기도 한다. 기본적으로 인덱스는 0부터 시작한다


# In[5]:


#index를 특별히 지정하지 않으면 0부터 시작
#index를 문자로 해도 됨


# In[6]:


list_data = [1, 2, 3, 4, 5]
list_name = ['a', 'b', 'c', 'd', 'e']
obj = Series(data = list_data, index = list_name)
print(obj)


# In[9]:


# 파이썬 딕셔너리를 이용해서 Series 생성하기
dic_data = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25} #JSON
dic_obj = Series(data = dic_data, dtype=np.float, name="mySeries")
print(dic_obj)


# In[10]:


# 데이터 참조하기
print(dic_obj["e"])


# In[11]:


# 특정 인덱스의 값 수정
dic_obj["e"] = 55.7
print(dic_obj)


# In[15]:


# value와 index를 각각 파이썬 리스트로 추출
print(dic_obj.values)
print(dic_obj.index)


# In[18]:


print(dic_obj[dic_obj > 22])


# In[19]:


print(dic_obj * 1.5) # 브로드 캐스팅


# In[21]:


print(dic_obj) # 원본에는 변화가 없다


# In[22]:


print(np.exp(dic_obj))


# In[25]:


# index가 있는지 없는지 확인하기 => k라는 인덱스가 있는지 알아본다
print("k" in dic_obj)
print("b" in dic_obj)


# ### NaN(Not a Number) => 데이터가 존재하지 않음

# In[32]:


# 파이썬 딕셔너리를 이용해서 Series 생성하기
dic_data = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25} #JSON
list_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dic_obj2 = Series(data = dic_data, index = list_name, dtype = np.float, name = "mySeries1")
print(dic_obj2)


# In[48]:


# NaN ==> 0으로 넣어보세요
dic_obj2.fillna(0)


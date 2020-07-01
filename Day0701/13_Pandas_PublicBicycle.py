#!/usr/bin/env python
# coding: utf-8

# ## 서울시 공공 자전거 대여정보 처리

# In[215]:


import pandas as pd
import numpy as np


# ### 1) 대여소 정보 읽어오기

# In[216]:


place = pd.read_excel("./data/서울특별시 공공자전거 대여소 정보(19.12.9).xlsx", delimiter = ",")
place


# In[217]:


#1) null이 들어가 있는가? 몇 개가 들어있는가?
place.isnull().sum().sum()


# In[218]:


#2) nan이 있는 컬럼 출력
place.columns[place.isnull().any()].tolist()


# In[219]:


place[place['대여소ID'].isnull() | place['대여소주소'].isnull() | place['위도'].isnull() | place['경도'].isnull() | place['기준시작일자'].isnull()]


# In[220]:


#3) nan 값을 삭제 ==> 전처리
place = place.dropna(axis = 0)
place


# In[8]:


#4) 대여소 ID의 타입 확인 후 ==> int32로 변환


# In[199]:


place['대여소ID'].dtypes


# In[235]:


place['대여소ID'].astype(int)


# In[236]:


place


# ### 2) 대여 정보 읽어오기

# In[225]:


rent_info = pd.read_csv("./data/서울특별시 공공자전거 대여정보_201911_2.csv", encoding = "cp949", delimiter=",")
rent_info


# In[226]:


#1) null이 들어가 있는가? 몇 개가 들어있는가?
rent_info.isnull().sum().sum()


# In[227]:


#2) nan이 있는 컬럼 출력
rent_info.columns[rent_info.isnull().any()].tolist()


# In[237]:


#3) nan 값을 삭제 ==> 전처리
rent_info = rent_info.dropna(axis = 0)
rent_info


# In[228]:


#4) 이용거리의 타입 확인 후 ==> int32로 변환
rent_info['이용거리'].dtypes


# In[230]:


rent_info['이용거리'].astype(int)


# In[231]:


rent_info


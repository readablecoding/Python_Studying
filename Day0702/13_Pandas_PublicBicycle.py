#!/usr/bin/env python
# coding: utf-8

# ## 서울시 공공 자전거 대여정보 처리

# In[58]:


import pandas as pd
import numpy as np


# ### 1) 대여소 정보 읽어오기

# In[59]:


place = pd.read_excel("./data/서울특별시 공공자전거 대여소 정보(19.12.9).xlsx", delimiter = ",")
place


# In[60]:


#1) null이 들어가 있는가? 몇 개가 들어있는가?
place.isnull().sum()


# In[61]:


#2) nan이 있는 컬럼 출력
place[place['대여소ID'].isnull()]


# In[62]:


#3) nan 값을 삭제 ==> 전처리
place = place.dropna()
place


# In[7]:


#4) 대여소 ID의 타입 확인 후 ==> int32로 변환


# In[63]:


place['대여소ID'].dtypes


# In[64]:


place = place.astype({"대여소ID" : np.int32})


# In[65]:


place


# In[36]:


# *** 대여소 정보


# In[37]:


#1) 대여소_구 종류 출력


# In[66]:


s1 = place.groupby("대여소_구").size()
s1


# In[38]:


#2) 대여소_구 평균 거치대 수


# In[91]:


s2 = place.groupby("대여소_구")["거치대수"].mean()
s2


# ### 2) 대여 정보 읽어오기

# In[68]:


rent_info = pd.read_csv("./data/서울특별시 공공자전거 대여정보_201911_2.csv", encoding = "cp949", delimiter=",")
rent_info


# In[69]:


#1) null이 들어가 있는가? 몇 개가 들어있는가?
rent_info.isnull().sum()


# In[30]:


#2) nan이 있는 컬럼 출력 ==> 없음


# In[31]:


#3) nan 값을 삭제 ==> 전처리 ==> 없음


# In[70]:


rent_info


# In[33]:


# *** 대여정보 데이터


# In[34]:


# 3)대여소 정보와 대여정보 데이터를 join


# In[71]:


s3 = pd.merge(place, rent_info, left_on = '대여소ID', right_on = '대여 대여소번호')
s3


# In[72]:


# 4)각 구별 평균 이용시간, 이용거리, 최대 이용시간, 최소 이용시간, 최대 이용거리, 최소 이용거리 -> agg 사용


# In[75]:


newGroup = s3.groupby("대여소_구")


# In[80]:


#평균 이용시간
newGroup["이용시간"].agg(np.mean)


# In[81]:


#평균 이용거리
newGroup["이용거리"].agg(np.mean)


# In[87]:


#이용거리 합
newGroup["이용거리"].agg(np.sum)


# In[82]:


#최대 이용시간
newGroup["이용시간"].agg(np.max)


# In[84]:


#최소 이용시간
newGroup["이용시간"].agg(np.min)


# In[85]:


#최대 이용거리
newGroup["이용거리"].agg(np.max)


# In[86]:


#최소 이용거리
newGroup["이용거리"].agg(np.min)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd


# ## 1)데이터 가져오기

# In[142]:


busStop = pd.read_csv("./data/광주 시내버스 정류소 현황(2017.6.19).csv", encoding = "cp949", delimiter=",")
del busStop["연번"]
busStop


# In[147]:


BIT = pd.read_csv("./data/광주광역시  버스운행정보시스템(BIT) 설치 현황(2017.6.16).csv", encoding = "cp949", delimiter=",")
del BIT["연번"]
BIT.isnull().sum()
BIT = BIT.fillna(0)
BIT


# ## 2) 조인

# In[144]:


newData = pd.merge(busStop, BIT, left_on = "코드번호", right_on = "단말기번호")
newData


# ## 3)전처리

# In[145]:


newData.dtypes


# In[146]:


newData = newData.astype({"경유노선수" : int, "설치년도" : int})
newData


# ## 4) 통계 처리

# In[167]:


#설치방소별 경우 노선수 합
newGroup = newData.groupby("설치장소")["경유노선수"].sum()
newGroup


# In[118]:


# 설치장소별 경유 노선수의 평균 
newGroup = newData.groupby("설치장소")
newGroup["경유노선수"].agg(np.mean)


# In[136]:


#설치장소별 가장 많이 설치된 수
newGroup = newData.groupby("설치장소")
newGroup["경유노선수"].agg(np.max)


# In[153]:


#설치장소별 가장 적게 설치된 수
newGroup = newData.groupby("설치장소")
newGroup["경유노선수"].agg(np.min)


# In[117]:


#설치년도별 버스운행정보시스템(BIT) 설치 수
newGroup2 = newData.groupby("설치년도")["정류소명"].count()
newGroup2


# In[152]:


#설치형태별 개수
newGroup3 = newData.groupby("설치형태")["정류소명"].count()
newGroup3


# In[155]:


#광주 북구 삼각동에 설치된 버스운행정보시스템의 수
newData[newData["설치장소"] == "북구 삼각동"]


# In[159]:


#광주 북구 삼각동에 설치된 버스운행정보시스템(BIT) 수
newData[newData["설치장소"] == "북구 삼각동"]["정류소명"].count()


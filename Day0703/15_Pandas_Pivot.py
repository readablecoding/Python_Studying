#!/usr/bin/env python
# coding: utf-8

# ## Pivot Table
# - 엑셀의 피봇테이블과 동일한 기능을 제공하는 판다스의 함수

# In[9]:


import numpy as np
import pandas as pd
import dateutil


# In[10]:


phone = pd.read_csv("./data/phone_data.csv")
phone


# In[11]:


phone["date"] = phone["date"].apply(dateutil.parser.parse, dayfirst = True) #날짜 포맷 변경
phone 


# In[17]:


phone.pivot_table(['duration'],
                  index = [phone.month, phone.item],
                  columns = [phone.network],
                  aggfunc = np.mean, #평균이라면 np.mean, 합계라면 sum
                  fill_value = 0 #NaN을 0으로 바꿈
                )


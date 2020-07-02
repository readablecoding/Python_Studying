#!/usr/bin/env python
# coding: utf-8

# # Groupby
# - SQL의 groupby

# In[2]:


import numpy as np
import pandas as pd


# In[39]:


data = pd.DataFrame(
    {"부서" : ["영업1팀", "영업1팀", "영업2팀", "해외영업팀", "해외영업팀", "영업1팀", "해외영업팀", "영업1팀", "해외영업팀", "영업1팀", "영업2팀", "해외영업팀"],
     "순위" : [1, 2, 1, 3, 2, 1, 1, 2, 3, 1, 2, 1],
     "연도" : [2014, 2015, 2015, 2014, 2017, 2017, 2019, 2019, 2020,2014, 2015, 2015],
     "매출액" : [876, 788, 900, 789, 657, 910, 987, 760, 670, 788, 980, 877]
    }
)
data


# In[40]:


data.groupby("부서")["매출액"].sum() #결과는 Series로 ...


# In[44]:


data.groupby("연도")["매출액"].sum() #결과는 Series로 ...


# In[43]:


multi = data.groupby(["부서", "연도"])["매출액"].sum()
multi


# In[45]:


multi.index


# In[46]:


multi["영업1팀" : "영업2팀"]


# In[47]:


multi.unstack().fillna(0)


# ## Aggregation

# In[48]:


myGroup = data.groupby("부서")


# In[50]:


for name, group in myGroup:
    print(name)
    print(group)


# In[51]:


group.agg(np.mean)


# In[52]:


myGroup.agg(np.mean)


# In[55]:


myGroup["매출액"].agg([np.sum, np.mean, np.max, np.min, ])


# ## filter()

# In[60]:


data.groupby("부서").filter(lambda x : len(x) > 3) #행의 개수가 3개 이상을 출력


# In[63]:


data.groupby("부서").filter(lambda x : x["매출액"].mean() > 880) 


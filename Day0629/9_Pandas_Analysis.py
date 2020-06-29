#!/usr/bin/env python
# coding: utf-8

# ### Grouping
# - 참고 : https://pandas.pydata.org/docs/reference/api/pandas.date_range.html

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.DataFrame({
    'A' : ['cho1', 'young1', 'cho1', 'young1', 'cho1', 'young1', 'cho1', 'young1'],
    'B' : ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'],
    'C' : np.random.randn(8),
    'D' : np.random.randn(8)    
})
df


# In[8]:


df.groupby('B').sum()


# In[10]:


df.groupby(['B', 'A']).sum()


# ## 시계열 데이터 다루기

# In[20]:


a = pd.date_range('20190101', periods = 10, freq='m') # H, M, S, D, m
a


# In[23]:


b = pd.date_range('20190101', periods = 5, freq= 'm')
ts = pd.Series(np.random.randn(len(b)), index = b)


# In[24]:


b


# In[25]:


ts


# In[26]:


ps = ts.to_period()
ps


# In[28]:


ps.to_timestamp()


# In[30]:


ps2 = pd.period_range('1990Q1', '1990Q2')
ps2


# In[33]:


ts = pd.Series(np.random.randn(len(ps2)), ps2)
ts


# In[34]:


ts.index = (ps2.asfreq('M', 'e') + 1).asfreq('H', 's') + 9 # asfreq( , )
ts.head()


# In[ ]:





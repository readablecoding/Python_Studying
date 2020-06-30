#!/usr/bin/env python
# coding: utf-8

# # DataFrame에서 다양한 연산을 수행하는 방법
# - add, sub, div, mul

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


a = pd.Series(range(1, 6), index = list('abcde'))
a


# In[4]:


b = pd.Series(range(4, 10), index = list('bcedfg'))
b


# In[6]:


a.add(b)


# In[7]:


a + b


# ## DataFrame을 이용하여 연산하기

# In[10]:


df1 = pd.DataFrame(np.arange(9).reshape(3, 3), columns = list("ABC"))
df1


# In[11]:


df2 = pd.DataFrame(np.arange(16).reshape(4, 4), columns = list("ABCD"))
df2


# In[12]:


df1 + df2


# ## Series + DataFrame

# In[13]:


df = pd.DataFrame(np.arange(16).reshape(4, 4), columns = list("ABCD"))
df


# In[14]:


s = pd.Series(np.arange(10, 14), index = list("ABCD"))
s


# In[16]:


df + s #DataFrame과 Series를 연산하면 컬럼을 기준으로 브로드캐스팅


# In[17]:


# DataFrame에는 컬럼명이 있다. 그런데 Series에는 컬럼명이 없다면?


# In[18]:


df = pd.DataFrame(np.arange(16).reshape(4, 4), columns = list("ABCD"))
df


# In[19]:


s = pd.Series(np.arange(10, 14))
s


# In[21]:


df + s #일치하는 컬럼명이 없으므로 브로드캐스팅이 일어나지도 않으며 데이터가 NaN이 된다


# In[24]:


df.add(s, axis = 0) # axis를 기준으로 브로드캐스팅이 일어남


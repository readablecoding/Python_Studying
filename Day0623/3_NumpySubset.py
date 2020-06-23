#!/usr/bin/env python
# coding: utf-8

# ## Numpy Indexing, Slicing
# - ndarray로부터 특정 요소를 가져오는 방법

# In[7]:


import numpy as np


# In[11]:


ary = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(ary)
print(ary[0][0])


# In[13]:


a = np.array(ary)
print(a)
print(a[0, 0]) #a의 0행 0열


# In[16]:


a[0, 0] = 12 
print(a)
print()
a[0, 0] = 55
print(a)


# ### Boolean Indexing
# - 배열의 각 요소의 값을 검사해서 그 여부가 True 인지 False인지 지정하는 방식
# - 특정 조건에 따라서 배열의 형태로 추출 가능

# In[26]:


import numpy as np


# In[27]:


a = np.arange(1, 25).reshape(4, 6)
print(a)


# In[28]:


even_ary = a % 2 == 0 #짝수인지 확인
print(even_ary)


# In[29]:


a = a[a % 2 == 0]
print(a)


# In[34]:


a = np.arange(1, 25).reshape(4, 6)
a = a[a % 2 != 0]
print(a)


# In[35]:


a = np.arange(1, 25).reshape(4, 6)
a = a[even_ary]
print(a)


# In[ ]:





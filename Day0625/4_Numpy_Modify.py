#!/usr/bin/env python
# coding: utf-8

# ## Numpy 배열의 변경
# - append, insert, delete
# - concatenate, vstack, hstack
# - hsplit, vsplit

# In[19]:


import numpy as np


# In[2]:


a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)


# In[3]:


print(a)


# In[4]:


print(b)


# ## append()
# - 2개의 배열을 합친 후 1차원으로 차원 축소
# - append()는 원본을 건드리지 않는다

# In[8]:



result = np.append(a, b)
print(result)


# In[9]:


print(a)


# In[11]:


# axis를 기준으로 append
# m x n : m => axis = 1 , n => axis = 0


# In[12]:


print(a)


# In[13]:


print(b)


# In[16]:


result1 = np.append(a, b, axis = 0) #세로(종) 기준으로 합침
print(result1)


# In[17]:


result2 = np.append(a, b, axis = 1) #가로(횡) 기준으로 합침
print(result2)


# ## insert()
# - 차원을 축소함

# In[18]:


a = np.arange(1, 10).reshape(3, 3)
print(a)


# In[25]:


print(np.insert(a, 1, 99)) #a의 인덱스 1번 위치에 99를 삽입하라


# In[23]:


print(np.insert(a, 1, 99, axis = 0)) #열의 1번째 위치에 99를 집어 넣음, 원본을 건드리지 않음


# In[27]:


print(np.insert(a, 1, 99, axis = 1)) #행의 1번째 위치를 기준으로 99를 집어 넣음


# ## delete()

# In[28]:


a = np.arange(1, 10).reshape(3, 3)
print(a)


# In[30]:


print(np.delete(a, 1)) #1번째 인덱스를 삭제함


# In[31]:


print(a)


# In[33]:


print(np.delete(a, 1, axis = 0)) #각각의 열에서 1번째 열의 값을 삭제하게 됨


# In[34]:


print(np.delete(a, 1, axis = 1)) #각각의 행에서 1번째 행의 값을 삭제하게 됨


# ## 배열의 결합
# - concatenate(), vstack(), hstack()
# 

# ## concatenate()

# In[43]:


import numpy as np


# In[44]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


# In[46]:


print(np.concatenate([a, b]))


# In[48]:


matrix = np.array([[1,2, 3], [4, 5, 6]]) #2행 3열
print(matrix)


# In[51]:


print(matrix.shape) #형태를 알려 줌


# In[53]:


print(np.concatenate([matrix, matrix], axis = 0))


# In[54]:


print(np.concatenate([matrix, matrix], axis = 1))


# In[56]:


print(matrix)


# In[72]:


a = np.array([10, 11, 12])
print(a)
b = np.array([[33], [33]])
print(b)


# In[59]:


print(np.vstack([a, matrix]))


# In[73]:


print(np.hstack([matrix, b]))


# In[74]:


print(np.hstack([b, matrix]))


# ## 배열 분리
# - 공유 폴더 : https://bit.ly/319Nllo
# - kilah@softsociety.net
# - kilah@naver.com

# In[77]:


import numpy as np


# In[78]:


data = np.arange(1, 25).reshape(4, 6)
print(data)


# In[80]:


a, b = np.hsplit(data, 2)
print(a)
print()
print(b)


# In[82]:


a, b, c = np.hsplit(data, 3)
print(a)
print()
print(b)
print()
print(c)


# In[86]:


a, b, c, d = np.hsplit(data, [1, 3, 5]) # a => [:, :1], b => [:, 1:3],  c => [:, 3:5], d => [:, 5:6]
print(data)
print()
print(a)
print()
print(b)
print()
print(c)
print()
print(d)


# In[89]:


# vsplit()의 사용
data = np.arange(1, 25).reshape(4, 6)
print(data)


# In[94]:


r1, r2, r3, r4 = np.vsplit(data, 4)
print(r1)
print()
print(r2)
print()
print(r3)
print()
print(r4)


# In[ ]:





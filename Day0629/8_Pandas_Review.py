#!/usr/bin/env python
# coding: utf-8

# # Pandas Review
# - 데이터를 분석하거나, AI를 하기위해 전 단계로 파일을 전처리하는 등의 처리를 위해 필요한 파이썬 라이브러리
# - 판다스의 데이터 구조는 Series, DataFrame 이다. -> 파이썬의 list, dictionary를 이용, 파일로부터 읽어들여 DataFrame을 
# 생성한 후 사용

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


pd.Series(list(range(5)), index=list(range(1, 10, 2)), dtype=np.float32)


# In[5]:


pd.DataFrame([5, 10, 15, 20, 25], index=['a', 'b', 'c', 'd', 'e'], columns=['Name'])


# In[6]:


pd.Series([1, 3, 5, 7, np.nan, 11, 13])


# In[10]:


#시계열 
dates = pd.date_range('20190101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df


# In[11]:


# Enum : 
df2 = pd.DataFrame({
    'A' : 10.5,
    'B' : pd.Timestamp('20190101'),
    'C' : pd.Series(5, index=list(range(0, 4)), dtype=np.float32),
    'D' : np.array([3] * 4, dtype=np.int32),
    'E' : pd.Categorical(['aaa', 'bbb', 'ccc', 'ddd']),
    'F' : 'Python'                   
})
df2


# In[12]:


df2.dtypes


# ## Pandas의 주요 속성 메소드
# - .index
# - .columns
# - .values
# - .T
# - .head(개수) / .tale(개수)
# - .describe(): 데이터 프레임의 통계정보 출력
# - .sort_index(): 행 이름이나 열 이름을 정렬, axis
# - .sort_values(by=컬럼명) 

# In[13]:


df.describe()


# In[15]:


df


# In[20]:


df.sort_values(axis=1, by='2019-01-02', ascending=False)


# ## 데이터 Selection

# ### 1) 이름을 이용한 Selection

# In[22]:


df


# In[25]:


df['A']


# In[26]:


type(df['A'])


# ### 2) Slicing을 이용한 Selection

# In[28]:


df[0 : 3]


# In[29]:


df['2019-01-01' : '2019-01-03']


# ### 3) .loc을 이용한 Selection

# In[31]:


df.loc[dates[0]]


# In[34]:


df.loc['2019-01-04':'2019-01-06', ['A', 'C']]


# In[36]:


df.loc[dates[0], ['A', 'C']]


# ### 4) .iloc을 이용한 Selection

# In[38]:


df.iloc[3]


# In[39]:


df.iloc[[1, 2, 4], [0, 2]]


# ### 5) .at을 이용한 Selection

# In[37]:


df.at[dates[0], 'A']


# ### 6) 조건을 이용한 선택 : 불리언 인덱싱

# In[43]:


df


# In[41]:


df[df > 0]


# In[45]:


df[df.C > 0]


# In[47]:


df2 = df.copy()
df2


# In[48]:


df2['E'] = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']


# In[49]:


df2


# In[54]:


df2[df2['E'].isin(['One', 'Two'])]


# ### Data 변경

# In[60]:


mySeries = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190102', periods=6))


# In[61]:


mySeries


# In[62]:


df2['F'] = mySeries
df2


# ### 결측치 처리하기
# - 결측치란 : 어떠한 이유든지 우리가 가진 데이터가 전부 측정되지 못하고 존재하지 못하는 경우가 발생할 수 있는데 이러한 데이터를 결측치라고 한다.
# - np.nan 라는 상수로 결측치를 나타낼 수 있다.
# - fillna(), dropna(), isna()

# In[63]:


df2.dropna(how='any')


# In[72]:


df1 = df.reindex(index=dates[0:3] , columns=list(['F']))
df1


# In[74]:


#df1.loc[dates[0] : dates[1], 'F'] = 1
df1.fillna(0)


# In[75]:


df1


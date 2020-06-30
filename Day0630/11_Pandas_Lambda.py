#!/usr/bin/env python
# coding: utf-8

# # Lambda 함수
# - 함수가 한 줄로 표현되며, 이름이 없는 익명함수로 선언할 때 사용
# - 현재 많은 프로그래밍 언어에서 람다식을 채용하고 있다

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


def f(x, y): # 함수 정의
    return x + y

f(10, 15) # 함수 호출


# In[5]:


(lambda x, y : x + y)(10, 15) # 함수를 정의하자마자 호출


# In[7]:


f = lambda x, y : x + y 
f(10, 15)


# In[8]:


f = lambda x : x ** 2
f(4)


# ## map 함수의 이용
# - map()은 함수와 시퀀스형 데이터를 인자로 받아서 각 요소마다 입력받은 함수를 적용한 후 반환
# - 일반적으로 전달하는 함수를 lambda 형태로 표현
# - 사용방법: map(function, sequence)  #sequence 타입으로 리턴하기

# In[9]:


lst = [1, 2, 3, 4, 5]
f = lambda x : x ** 2

list(map(f, lst)) #새로운 시퀀스를 리턴


# In[16]:


f1 = lambda x, y : x * y
lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 11, 12, 13, 14]

list(map(f1, lst1, lst2))


# ## map 함수를 Series에 적용

# In[17]:


s1 = pd.Series(np.arange(10))
s1


# In[19]:


list(map(lambda x : x ** 2, s1))


# In[20]:


s1.map(lambda x : x ** 2)


# ## map 함수를 이용해서 데이터 수정

# In[21]:


s1 = pd.Series(np.arange(10))
s1


# In[24]:


dic = {1 : 'A', 2 : 'B', 3 : 'C'} 
s1.map(dic)


# In[29]:


s2 = pd.Series(np.arange(10, 20))
s1.map(s2)


# ## map()을 DataFraame에 적용

# In[50]:


df = pd.read_csv("./data/wages.csv")
df.head(10)


# In[51]:


df.race.unique() #범주를 확인하는 용도로 .dataframe명.unique()


# In[46]:


# 성별을 0, 1로 수정하고자 하면
# 1) replace로 써도 된다 -> 원본이 바뀐다


# In[52]:


#새로 컬럼명을 만들어 0과 1을 집어 넣음
df["code"] = df.sex.map({"male" : 0, "female" : 1})
df


# In[53]:


del df["code"]
df


# ## replace()를 이용하여 데이터 값 수정

# In[54]:


# inplace = True 옵션을 줄 경우 변경된 값을 원본에 적용
df.sex.replace(["male", "female"], [0, 1], inplace = True)


# In[41]:


df


# ## apply()함수의 사용

# In[59]:


df_sample = df[["earn", "height", "age"]]
df_sample.head()


# In[60]:


f = lambda x : x.max() - x.min()


# In[61]:


df_sample.apply(f) #apoly 함수는 람다를 전달인수로 받아 


# In[63]:


def fx(x) :
    return pd.Series([x.max(), x.min()], index = ["max", "min"])


# In[66]:


df_sample.apply(fx)


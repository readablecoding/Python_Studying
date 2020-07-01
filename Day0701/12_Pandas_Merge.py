#!/usr/bin/env python
# coding: utf-8

# ##  DataFrame Merge

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


# 두 DataFrame에서 공통열(PK, FK)이 필요
df1 = pd.DataFrame({
    '번호' : [10, 20, 30, 40, 50, 60, 70],
    '이름' : ['홍길동', '임꺽정', '전우치', '손오공', '저팔계', '사오정', '삼장법사']
})
df1


# In[12]:


df2 = pd.DataFrame({
    '번호' : [10, 10, 20, 40, 50, 40, 40, 70, 80],
    '금액' : [1000, 2500, 4500, 3400, 1100, 230, 3400, 3550, 3511]
})
df2


# In[14]:


pd.merge(df1, df2) # inner join


# In[16]:


pd.merge(df1, df2, how = 'outer') # full outer join


# In[17]:


pd.merge(df1, df2, how = 'left') # left outer join


# In[18]:


pd.merge(df1, df2, how = 'right') #right outer join


# ## Join on

# In[21]:


# 두 DataFrame에서 공통열(PK, FK)이 필요
df1 = pd.DataFrame({
    '번호' : [10, 20, 30, 40, 50, 60, 70],
    '이름' : ['홍길동', '임꺽정', '전우치', '손오공', '저팔계', '사오정', '삼장법사'],
    '타입' : ['우수', '일반', '우수', '우수', '일반', '일반', '우수']
})
df1


# In[29]:


df2 = pd.DataFrame({
    '고객번호' : [10, 10, 20, 40, 50, 40, 40, 70, 80],
    '금액' : [1000, 2500, 4500, 3400, 1100, 230, 3400, 3550, 3511],
})
df2


# In[34]:


pd.merge(df1, df2, left_on = '번호', right_on = '고객번호') # 공통 컬럼명이 없을 경우 오류 발생


# ## [연습]

# In[47]:


staff = pd.DataFrame([
    {'이름' : '홍길동', '부서' : '영업부'},
    {'이름' : '임꺽정', '부서' : '개밭팀'},
    {'이름' : '전우치', '부서' : 'R&D'},
    {'이름' : '손오공', '부서' : '개발팀'},
    {'이름' : '저팔계', '부서' : '영업부'},   
])
staff


# In[48]:


education = pd.DataFrame([{'성명' : '홍길동', '학교' : '가나다대학교', '전공' : '컴퓨터'},
                          {'성명' : '임꺽정', '학교' : '나다대학교', '전공' : '미디어'},
                          {'성명' : '손오공', '학교' : '가다대학교', '전공' : '통신'},
                          {'성명' : '저팔계', '학교' : '가다대학교', '전공' : '전자정보'},
                          {'성명' : '사오정', '학교' : '파하대학교', '전공' : '응용미술'},                                                                     
])
education


# In[57]:


# 1) 이름 학교 전공 부서


# In[69]:


sample1 = pd.merge(staff, education, left_on = '이름', right_on = '성명')
sample2 = sample1.loc[:, ['이름', '학교', '전공', '부서']]
sample2


# In[58]:


# 2) 이름 전공 부서


# In[70]:


sample1 = pd.merge(staff, education, left_on = '이름', right_on = '성명')
sample2 = sample1.loc[:, ['이름', '전공', '부서']]
sample2


# In[77]:


#두 테이블 연결
pd.concat([staff, staff])


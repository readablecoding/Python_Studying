import util #같은 디렉토리에 있어야 가져올 수 있다

print("1 inch = ", util.INCH, "cm") #1 inch =  2.54 cm

print("1 ~ 10까지의 합계:", util.sum(10)) #1 ~ 10까지의 합계: 55

import sys

print(sys.path) #디렉토리를 문자열로 나타내는
"""
['c:\\workspace\\Day0605', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32', 
'C:\\Users\\user\\AppData\\Roaming\\Python\\Python38\\site-packages', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']

c:\\workspace\\Day0605가 첫번째 경로로 나타남
"""

sys.path.append("C:\\workspace\\Day0604") #다른 경로에 있는 모듈 가져오기

# import Test02 
"""
1591330666.4857507
Fri Jun  5 13:17:46 2020
time.struct_time(tm_year=2020, tm_mon=6, tm_mday=5, tm_hour=13, tm_min=17, tm_sec=46, tm_wday=4, tm_yday=157, tm_isdst=0)
time.struct_time(tm_year=2020, tm_mon=6, tm_mday=5, tm_hour=4, tm_min=17, tm_sec=46, tm_wday=4, tm_yday=157, tm_isdst=0)
"""
#Test02.__name__: Test02

sys.path.append("C:\\workspace\\Day0605\\testpack")

import testpack.dir1.mod1 as mod1

mod1.func1() #저는 mod1입니다.

from testpack.dir2 import mod2  #디렉토리를 정해서 가져옴
mod2.func2() #저는 mod2입니다.

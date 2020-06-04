# import math
# print(math.pi) #3.141592653589793
# print(dir(math)) #dir()는 모듈 안의 요소를 확인하는 용도
# help(math.ceil) #help()는 사용법, 튜토리얼을 확인하는 용도
"""
elp on built-in function ceil in module math:

ceil(x, /)
    Return the ceiling of x as an Integral.
"""

# from math import pi #math에서 pi만 가져오겠다
# print(pi) #3.141592653589793

import time
print(time.time()) #에폭 시간, 1591245817.63888
print(time.ctime()) #현재 시간 문자열, Thu Jun  4 13:43:37 2020
print(time.localtime()) #지역 시간 전용 객체
"""
time.struct_time(tm_year=2020, tm_mon=6, tm_mday=4, tm_hour=13, tm_min=43, tm_sec=37, tm_wday=3, tm_yday=156, tm_isdst=0)
"""
print(time.gmtime()) #UTC 시간 전용 객체
"""
time.struct_time(tm_year=2020, tm_mon=6, tm_mday=4, tm_hour=4, tm_min=43, tm_sec=37, tm_wday=3, tm_yday=156, tm_isdst=0)
"""


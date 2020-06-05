try:
    a = int("aaaa")
    print(a)
except:
    print("예외 발생") #예외 발생

# a = int("aaaa") #ValueError: invalid literal for int() with base 10: 'aaaa'  

#a = int([12, 34]) #TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

try:
    a = str(9999)
    print(a[5])
except (ValueError, IndexError) as e:
    print("ValueError 발생") #ValueError 발생
# except IndexError as e: #예외를 별칭을 통해 객체로 표현함
#     print("IndexError 발생")
#     print(e) #string index out of range 
#     print(dir(e))
except: #마지막에 그냥 except를 붙이기도 함
    pass


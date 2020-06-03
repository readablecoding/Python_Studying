#property 사용
# class Date:
#     def __init__(self, month): #생성자
#         self.inner_month = month
#     def getMonth(self): #getter
#         return self.inner_month
#     def setMonth(self, month): #setter
#         self.inner_month = month
#     Month = property(getMonth, setMonth) #1다리 더 걸쳐서 정보은닉, 새로운 변수에 getter, setter를 저장


# day = Date(7)
# #day.setMonth(8)
# #print(day.getMonth())

# day.Month = 8
# print(day.Month) #8

#데커레이터 사용
# class Date:
#     def __init__(self, month): #생성자
#         self.inner_month = month
   
#     @property #getter 
#     def Month(self):
#         return self.inner_month
    
#     @Month.setter #setter
#     def Month(self, month):
#         self.inner_month = month

class Date:
    def __init__(self, month): #생성자
        self.__month = month
        
    @property
    def Month(self): #getter
        return self.__month

    @Month.setter
    def Month(self, month): #setter
        self.__month = month
    


day = Date(7)
day.Month = 8
print(day.Month) #8

day.inner_month = 9 #정보 은닉이 있어도 public이므로 접근 가능
print(day.inner_month) #9


day.__month = 9 
print(day.__month) #9

print(day._Date__month) #8



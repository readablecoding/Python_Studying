# class Car:
#     def __init__(self):
#         self.__color = "빨강" #private
    
# red_car = Car()

# print(red_car._Car__color) #빨강 -> _클래스명__변수명 형태로 해야 한다

# print(dir(red_car)) #dir()를 통해 객체가 가진 모든 요소를 문자열로 나타냄


class Human:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

kim = Human("김씨")
kim2 = Human("김씨")

print("kim id:",id(kim)) #11170168
print("kim2 id:", id(kim2)) #11170336

print("kim == kim2:", kim == kim2) #kim == kim2: True


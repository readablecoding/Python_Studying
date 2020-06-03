# class Human:
#     age = 30

# new_Human = Human() #객체화
# print(new_Human) #<__main__.Human object at 0x014E7178> 
# print(type(new_Human)) #<class '__main__.Human'>
# print(new_Human.age) #30

class Human:
    age = 30 #age = 30는 스태틱 필드

    def __init__(self, height):
        self.height = height #self.height는 멤버 필드, = height를 통해 초기화
new_Human = Human(175.0)
new_Human2 = Human(178.0)
print(type(new_Human))
Human.age += 1     #클래스를 통한 접근 -> 좀 더 권장하는
new_Human.age += 1 #인스턴스로 접근

print("Human.age:", Human.age) #Human.age: 31
print("new_Human.age:", new_Human.age) #new_Human.age: 32
print("new_Human.age2:", new_Human2.age) #new_Human.age2: 31
print("new_Human.height:", new_Human.height) #new_Human.height: 175.0
print("new_Human.height2:", new_Human2.height) #new_Human.height2: 178.0



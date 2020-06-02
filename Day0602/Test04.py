a, b, c = 10, 20, 30 #전역변수

def func():  
    b = 200 #지역변수
    global c #global 키워드를 통해 전역변수로 바꿈
    c = 300
    print("a:", a, "b:", b, "c:", c) #a: 10 b: 200 c: 300

func()
print("a:", a, "b:", b, "c:", c) #a: 10 b: 20 c: 300

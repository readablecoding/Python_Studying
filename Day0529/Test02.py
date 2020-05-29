#튜플 언팩킹(tupple unpacking)
#여러 개의 변수를 한꺼번에 초기화하는 것
breakfast, lunch, dinner = \
("토스트", "김밥", "스테이크")
print("breakfast: ", breakfast)
print("lunch: ", lunch)
print("dinner: ", dinner)
#파이썬에서는 다음 줄로 옮겨 쓰는 것이 안된다
#그래서 \(역슬래시)를 넣어주면 다음 줄에서 계속 작성하겠다는 것을 말한다

#자바
#a = 10
#b = 20
#temp = a
#a = b
#b = temp
#print(a, b) #20, 10

#파이썬
a, b = (10, 20)
a, b = b, a #새로운 튜플을 만들어 대입
print(a, b) #v







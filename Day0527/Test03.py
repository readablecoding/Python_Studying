print(10 / 3) #3.3333333333333335, 정수와 정수를 나눠도 실수로 나옴
print(10 // 3) #3 -> 몫
print(10 % 3) #1 -> 나머지
print(10 ** 3) #1000 -> 거듭제곱

a = "1"
b = "1"
c = 1
d = str(1) # "1"

print("a == b", a == b)
print("a is b", a is b) #같은 메모리를 참조하니 참이 나온다
print("a == c", a == c) #a == c False
print("a is c", a is c) #a is c False
print("a == d", a == d) #a == d True -> 같은 값이니 참이 나옴
print("a is d", a is d) #a is d False -> 같은 객체인지 물어 봄

#메모리 주소 찾기
print(id(a)) #29722560
print(id(b)) #29722560
print(id(d)) #57645632

#객체 비교 연산자(is, is not)
e = False
f = bool(0)

print("e == f", e == f) #e == f True
print("e is f", e is f) #e is f True
#true, false, none은 하나의 객체만 참조한다
# ==보다는 is를 써서 비교하는 것이 관례

g = None
h = None
print("g == h", g == h) #g == h True
print("g is h", g is h) #g is h True
# None의 경우 is를 써서 비교하기

#멤버십 연산자(in, not in)
#대소문자를 구분한다
#객체로는 반복 가능한 객체가 온다, str 또한 반복 객체다
str1 = "Python is Fun!"
print("P" in str1) #True
print("Python" in str1) #True
print("Java" not in str1) #True

#iterable
print(1 in [1, 2, 3]) #True




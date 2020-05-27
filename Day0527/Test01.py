a = 10
print(a) #10
print(type(a)) #<class 'int'>

b = 0b1010 #2진수 표기 
c = 0o1010 #8진수 표기 
d = 0x1010 #16진수 표기 

print(b) #10
print(c) #520
print(d) #4112

#반환형이 string
print(bin(b)) #0b1010
print(oct(c)) #0o1010
print(hex(d)) #0x1010

e = 3.14
f = 3.14e-10

print(e) #3.14
print(f) #3.14e-10
print(type(e)) #<class 'float'>
print(type(f)) #<class 'float'>

#raw 문자열 작성
g = r"c:\the folder"
print(g) #c:\the folder
print(type(g)) #<class 'str'>

h = "Hello"
i = "World"
print(h + i) #HelloWorld
print("=" * 30) #==============================
#print("SWDO" + 3 + "기!") #에러 발생, 문자열과 숫자 간의 연결 불가

j = ord("A")
k = chr(97)
print(j) #65
print(k) #a

l = True
m = False
print(type(l)) #<class 'bool'>
print(type(m)) #<class 'bool'>

if "": 
    print("참입니다!") 
else:
    print("거짓입니다!") #거짓입니다!

n = int(True)
print(n)
print(type(n)) 




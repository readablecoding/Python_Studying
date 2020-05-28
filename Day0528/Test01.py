a = "Python is Fun!"
print(a[0]) #P
print(a[-1]) #! -> 마이너스 인덱스는 뒤부터 시작
print(a[0 : 6]) #Python -> 0번 인덱스부터 5번까지의 문자열, 자바의 substring과 비슷
print(a[-4 : -1]) #Fun
print(a[:6]) #Python -> 번호를 생략하면 시작부터를 말한다
print(a[-4:]) #Fun! -> 맨 뒤까지의 문자열
print(a[:]) #Python is Fun! -> 둘 다 생략하면 처음부터 끝까지 나타냄

#문자열의 길이 반환
print(len(a)) #14
#자바에서는 a.length()라고 했었다

print("=" * 30)

print(a.find("n")) #5 -> python의 n이 나온다
print(a.rfind("n")) #12 -> fun의 n이 나온다

print(a.find("Java")) #-1
#print(a.index("Java")) #예외를 일이킨다
print("=" * 30)

print(a.count("n")) #2
b = ""
print(b.isascii()) #True
print("=" * 30)
str_list = ["ⅷ", "¾", "2³", "3", "3.14"]
for str in str_list:
    print(str, ".isnumeric(): ", str. isnumeric())
    print(str, ".isdigit(): ", str.isdigit())
    print(str, ".isdecimal(): ", str.isdecimal())
    print("-" * 5)

"""
ⅷ .isnumeric():  True
ⅷ .isdigit():  False
ⅷ .isdecimal():  False
-----
¾ .isnumeric():  True
¾ .isdigit():  False
¾ .isdecimal():  False
-----
2³ .isnumeric():  True
2³ .isdigit():  True
2³ .isdecimal():  False
-----
3 .isnumeric():  True
3 .isdigit():  True
3 .isdecimal():  True
-----
3.14 .isnumeric():  False
3.14 .isdigit():  False
3.14 .isdecimal():  False
-----
"""

print("=" * 30)
print(a.replace("Fun", "interesting")) #Python is interesting!
#replace라는 결과로 a라는 문자열이 바뀐 것이 아니라 새로운 문자열이 반환된 것이다

print("=" * 30)
print(a[:6].rjust(10)) #    Python -> 10개의 문자를 받는데 우측 정렬이 된 것이다
print(a[:6].rjust(3)) #Python -> 정렬이 되지는 않고 문자만 출력됨

print(a.split()) #['Python', 'is', 'Fun!'] -> 공백을 기준으로 잘라 리스트 형태로 나타냄
print(a.split("n")) #['Pytho', ' is Fu', '!'] -> 부분자는 포함되지 않는다
#print(a.split("")) #에러 발생, 일일히 1글자씩 쪼갤 때는 안된다

#문자열을 한 글자씩 자르려면?
print([str for str in a])
#['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'F', 'u', 'n', '!']

#리스트에 구분 문자열로 추가해 문자열 반환
print("*".join(["Python", "is", "Fun!"])) #Python*is*Fun!




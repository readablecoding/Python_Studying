#형식 문자를 이용한 포매팅
num = 10
days = "ten"
str = "I ate %d apples. So I was sick %s days." % (num, days)
print(str) #I ate 10 apples. So I was sick ten days.

print("=" * 30)

#format() 함수
str2 = "I ate {n} apples. So I was sick {0} days.".format(days, n = num)
#I ate 10 apples. So I was sick ten days.
#전달인수, 키워드 인수 순으로 받아야 한다



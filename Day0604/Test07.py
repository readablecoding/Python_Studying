print(0.1 + 0.2) #0.30000000000000004 -> 오차가 붙기 때문
print(0.1 + 0.2 == 0.3) #False

import decimal
a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
print(a) #0.1
print(b) #0.2
print(a + b) #0.3 -> 정확하게 연산을 하니 0.3이 나옴

#분수 표현 클래스
import fractions
a = fractions.Fraction(3, 10) #분자 분모
b = fractions.Fraction(-2, 20)
print(a) #3/10
print(b) #-1/10
print(a + b) #1/5
print(a + 1) #13/10
print(a - 2) #-17/10
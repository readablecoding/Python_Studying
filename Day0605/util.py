INCH = 2.54 #변수를 상수 취급하기 위해 대문자로 표현, 값을 변경 가능

def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result



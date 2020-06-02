#인수의 기본값
# def calc(num, div = 1): #기본값은 인수의 오른쪽에 위치하기
#     if div == 0:
#         return (0, 0)
#     else:
#         return (num // div, num % div)

# print(calc(20, 3)) #(6, 2)
# print(calc(20, 0)) #(0, 0) 
# print(calc(20)) #(20, 0) -> div를 전달하지 않아 기본값으로 설정한 1로 나눔

#키워드 인수
# def calc(begin, end, step):
#     sum = 0
#     for num in range(begin, end + 1, step):
#         sum += num
#     return sum

# print(calc(3, 5, step = 1)) #12

# print(calc(step = 1, end = 5, begin = 3)) #12
# #print(calc(3, step = 1, 5)) #SyntaxError: positional argument follows keyword argument
# print(calc(3, step = 1, end = 5)) #12

#가변 인수
# def calc(anything, *nums): #가변 인수는 가장 마지막에 위치함
#     print(anything)
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(calc(1, 3, 5)) 
# print(calc(5, 6, 7, 8, 9)) 

#키워드 가변 인수
def calc(*nums, **options):
    result = 0
    for num in nums:
        if "sum" in options and options["sum"]:
            result += num
        elif "sub" in options and options["sub"]:
            result -= num
    
    return result

print(calc(1, 2, 3, sum = True)) #30
print(calc(1, 2, 3, sub = True)) #6
print(calc(1, 2, 3, sum = False, sub= True)) #-6
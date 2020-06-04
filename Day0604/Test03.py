import time

def func1():
    list = []
    for i in range(1000000):
        list.append(i)
    return list

def func2():
    list = [i for i in range(1000000)]
    return list

start = time.time()
func1()
end = time.time()
print("함수 1 실행:", end-start, "초") #함수 1 실행: 0.24733686447143555 초

start = time.time()
func2()
end = time.time()
print("함수 2 실행:", end-start, "초") #함수 2 실행: 0.16057181358337402 초


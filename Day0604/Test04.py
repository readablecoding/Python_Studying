import time

print("CountDown!")
time.sleep(1) #프로그램을 숫자 만큼 중단
for i in range(1, 4):
    print(4-i)
    time.sleep(1)
print(0)
print("The end")

"""
CountDown!
3
2
1
0
The end
"""
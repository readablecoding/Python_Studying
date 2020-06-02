#20 이하의 소수
prime_list = [i for i in range(2, 21) if all(i % j != 0 for j in range(2, i))]
print(prime_list) #[2, 3, 5, 7, 11, 13, 17, 19]

#20 이하의 합성수
composite_list = [i for i in range(2, 21) if any(i % j == 0 for j in range(2, i))]
print(composite_list) #[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

a = [0, 1, 2, [3, 4, 5]]
b = a
c = a[:]
import copy
d = copy.copy(a)
e = copy.deepcopy(a)

a[0] = 100
a[3][2] = -100

print("원본:", a) #[100, 1, 2, [3, 4, -100]]
print("직접 대입:", b) #[100, 1, 2, [3, 4, -100]]
print("슬라이싱으로 복사:", c) #[0, 1, 2, [3, 4, -100]]
print("얕은 복사:", d) #[0, 1, 2, [3, 4, -100]]
print("깊은 복사:",e ) #[0, 1, 2, [3, 4, 5]] -> 중첩 리스트를 가장 완벽하게 복사

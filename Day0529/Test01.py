#인덱스
l = [0, 1, 2]
l[1] = [3, 4, 5]
print(l) #[0, [3, 4, 5], 2] - 3개의 요소를 가진 리스트

#슬라이싱
l = [0, 1, 2]
l[1:1] = [3, 4, 5]
print(l) #[0, 3, 4, 5, 1, 2] -> 슬라이싱을 통해 변경

#insert 함수
l = [0, 1, 2]
l.insert(1, [3, 4, 5])
print(l) #[0, [3, 4, 5], 1, 2] -> 삽입하는 방식

num_list = list(range(1, 11))
#자바였다면 numList로 표현
print(num_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_list.remove(3) #값 3을 지운다
print(num_list) #[1, 2, 4, 5, 6, 7, 8, 9, 10]

del num_list[3] #3번째 요소를 지운다
print(num_list) #[1, 2, 4, 6, 7, 8, 9, 10]

del num_list[3:6] #3번부터 5번 요소까지 지운다
print(num_list) #[1, 2, 4, 9, 10]

str_list = list("python")
print(str_list) #['P', 'y', 't', 'h', 'o', 'n']
print(len(str_list)) #6
print(min(str_list)) #h -> 아스키 코드 값을 기준으로 계산함
print(max(str_list)) #y -> 아스키 코드 값을 기준으로 계산함
print(str_list.index("o")) #4
print("z" in str_list) #False -> 요소 in 객체


list1 = ["A","B","C"]
list2 = ["D", "E", "F"]
print("list1", list1)
print("list2", list2)

list3 = list1 + list2
print("list1", list1) #list1 ['A', 'B', 'C']
print("list2", list2) #list2 ['D', 'E', 'F']
print("list3", list3) #list3 ['A', 'B', 'C', 'D', 'E', 'F']

list1.extend(list2)
print("list1", list1) #list1 ['A', 'B', 'C', 'D', 'E', 'F']
print("list2", list2) #list2 ['D', 'E', 'F']
print("list3", list3) #list3 ['A', 'B', 'C', 'D', 'E', 'F']

list4 = list1 * 3
print("list1", list1) #list1 ['A', 'B', 'C', 'D', 'E', 'F'] 
print("list2", list2) #list2 ['D', 'E', 'F']
print("list3", list3) #list3 ['A', 'B', 'C', 'D', 'E', 'F'] 
print("list4", list4) #list4 ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']



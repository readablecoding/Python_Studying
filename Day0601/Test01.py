s = set() 
print(type(s)) #<class 'set'>

basket = {"apple", "banana", "orange", "apple", "orange"}
print(basket) #{'banana', 'orange', 'apple'} -> 순서가 없고 중복이 안된다

spell = set("abracadabra")
print(spell) #{'a', 'r', 'c', 'b', 'd'}

prime1 = {2, 3, 5, 7}
prime2 = {11, 13, 15, 17}

prime1.add(9) #요소를 추가
prime1.remove(9) #요소를 제거
prime1.update(prime2) #집합을 병합

print("소수 집합1:", prime1) #소수 집합1: {2, 3, 5, 7, 11, 13, 15, 17}
print("소수 집합2:", prime2) #소수 집합2: {17, 11, 13, 15} ->집합에는 순서가 없다




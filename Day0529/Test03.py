new_dict = {0: "Hello"}
print(new_dict) #{0: 'Hello'}

#요소 추가
#인덱스, 슬라이싱이 불가
new_dict[1] = "World"
print(new_dict) #{0: 'Hello', 1: 'World'}

new_dict[0] = "hi"
print(new_dict) #{0: 'hi', 1: 'World'}

del new_dict[0] #키가 0인 것의 값을 삭제
print(new_dict) #{1: 'World'}
#del new_dict[0] #KeyError: 0

print(new_dict.pop(1)) #World -> 원본에서 삭제됨
print(new_dict) #{} -> 빈 사전이 됨

d = {1: "one", 3: "three", 2: "two", 0: "zero"}
print(min(d)) #0 -> 키 중에서 가장 작은 값
print(max(d)) #3 -> 키 중에서 가장 큰 값
print(sorted(d)) #[0, 1, 2, 3] -> 원본에 영향을 주지 않고 키가 정렬된 새로운 리스트가 만들어짐
#사전은 순서가 없으니까 정렬할 수가 없다. 키라도 추출해 정렬한 새로운 리스트를 만들어 반환

stocks = {"egg": 500, "sausage": 300, "bacon": 200}
keys = stocks.keys()
values = stocks.values()
items = stocks.items()
# print(keys) #dict_keys(['egg', 'sausage', 'bacon'])
# print(values) #dict_values([500, 300, 200])
# print(items) #dict_items([('egg', 500), ('sausage', 300), ('bacon', 200)]) -> 리스트처럼 사용 가능

for key in keys:
    print("품목명:", key, ",재고량:", stocks.get(key))
"""
품목명: egg ,재고량: 500
품목명: sausage ,재고량: 300
품목명: bacon ,재고량: 200
"""
print("=" * 30)
for item in items:
    print("품목명:", item[0], ",재고량:", item[1])
"""
품목명: egg ,재고량: 500
품목명: sausage ,재고량: 300
품목명: bacon ,재고량: 200
"""
print("=" * 30)
n = 0
for val in values:
    n += val
print("총 재고량:", n) #총 재고량: 1000


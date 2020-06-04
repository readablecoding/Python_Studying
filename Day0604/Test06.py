import random

# menu_list = ["김밥", "떡볶이", "순대", "라면"]
# print("오늘의 메뉴:", random.choice(menu_list)) #오늘의 메뉴: 순대

#로또 번호 추출
num_list = [i for i in range(1, 46)]
rotto = random.sample(num_list, 6)
print("로또 번호:", rotto) # 로또 번호: [24, 1, 44, 28, 21, 36]
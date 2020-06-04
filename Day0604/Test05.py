import calendar

# print(calendar.calendar(2020))
# calendar.prcal(2020)

# print(calendar.month(2020, 6))
# calendar.prcal(2020, 6)

# year = int(input("년도를 입력하세요:")) #년도를 입력하세요:2021
# print(year, "년은", "윤년입니다." if calendar.isleap(year) else "평년입니다.") #2021 년은 평년입니다.

weekdays = ["월", "화", "수", "목", "금", "토", "일"]
print(2020, "년", 6, "월", 4, "일은", weekdays[calendar.weekday(2020, 6, 4)], "요일 입니다")


class MyException(Exception):
    def __init__(self): #생성자
        super().__init__("사용자 정의 예외 발생") #super()를 통해 부모의 생성자 호출

try:
    raise MyException #사용자 정의 예외 가져옴
except MyException as me: 
    print(me) #사용자 정의 예외 발생

try:
    assert 1 == "1", "assertionError 발생" 
except AssertionError as ae:
    print(ae) #assertionError 발생

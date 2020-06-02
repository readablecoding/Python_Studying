#함수
def echo(anything):
    print(anything)
    return "네, 안녕하세요!"
a = echo("안녕하세요?") #함수의 실행 결과를 변수에 전달
print(a) #네, 안녕하세요!

# 함수를 값처럼 저장했으니 b가 함수처럼 작동한다
b = echo
print(b) #<function echo at 0x015E7070>
b("안녕!") #안녕!

#def calc(): #SyntaxError: unexpected EOF while parsing 

def calc():
    pass #에러 발생을 막는다. 아무런 동작을 안 한다
calc()

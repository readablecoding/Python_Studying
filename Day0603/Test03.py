class Car:
    @staticmethod
    def hello(): #정적 메서드는 인수를 받지 않는다
        print("안전운전하세요!")

    count = 0 #스태틱 필드

    def __init__(self, color): #생성자
        self.color = color
        Car.count += 1 #생성자를 통해 1씩 증가

    @classmethod #스태틱 변수는 클래스 메소드를 쓰는 것이 좋다
    def outcount(cls): #클래스를 인수로 받음
        print(cls.count) #클래스의 count를 출력

blue_car = Car("blue")
red_car = Car("Red")

Car.outcount() #2 -> 클래스 메소드를 통해 접근, 클래스명.함수명
print("blue_car.count:", blue_car.count) #blue_car.count: 2 -> 인스턴스를 통해 접근
print("red_car.count:", red_car.count) #red_car.count: 2

Car.hello() #안전운전하세요! -> 클래스를 통해 접근 가능 
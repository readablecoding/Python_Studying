class Parent:
    family_name = "김"

    #일반 메소드
    def name_by_common(self):
        return self.family_name


    @classmethod #클래스 메소드
    def name_by_class(cls): #인수가 클래스
        return cls.family_name


    @staticmethod #스태틱 메소드
    def name_by_static():
        return Parent.family_name

mother = Parent()
print("부모 클래스에서 일반 함수를 통해 확인한 성씨:", mother.name_by_common()) #김
print("부모 클래스에서 클래스 메서드를 통해 확인한 성씨:", Parent.name_by_class()) #김
print("부모 클래스에서 스태틱 메서드를 통해 확인한 성씨:", Parent.name_by_static()) #김

print("=" * 30)
class Child(Parent): #상속 Child가 Parent를 상속함
    family_name = "이"

son = Child()

print("자식 클래스에서 일반 함수를 통해 확인한 성씨:", son.name_by_common()) #이
print("자식 클래스에서 클래스 메서드를 통해 확인한 성씨:", Child.name_by_class()) #이 -> Child 클래스가 전달돼 이씨가 나옴
print("자식 클래스에서 스태틱 메서드를 통해 확인한 성씨:", Child.name_by_static()) #김 -> 호출은 되지만 인수가 없어 자기 자신의 패밀리네임인 부모의 성인 김이 나옴
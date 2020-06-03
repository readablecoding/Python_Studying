class Human:
    def __init__(self, age):
        self.age = age

    def __len__(self):
        return self.age


kim = Human(30)
lee = Human(25)
print(len(kim)) #30
print(len(lee)) #25
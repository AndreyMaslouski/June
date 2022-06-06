# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

# Метод объекта (экземпляра), обычный метод:

class Person:
    age_1 = 15
    age_2 = 17
    def __init__(self,name):
        self.name_1 = name
        self.name_2 = name

    def __del__(self):
        print(self.name_1,"удален из памяти")


    def Info(self):
        print(self.age_1)
        print(self.age_2)
        print("Привет, меня зовут",self.name_1)
        print("Мне",self.age_1,"лет")
        print("Привет, меня зовут", self.name_2)
        print("Мне", self.age_2, "лет")

person_1 = Person("Mikle")
person_1.Info()
del person_1
person_2 = Person("Никита")
person_2.Info()




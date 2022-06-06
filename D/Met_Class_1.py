# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

# Метод объекта (экземпляра), обычный метод:

class Person:
    age_1 = 15
    age_2 = 17
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print(self.name,"удален из памяти")


    def Info(self):
        print(self.age_1)
        print(self.age_2)
        print("Привет, меня зовут",self.name)
        print("Мне",self.age_1,"лет")
        print("Привет, меня зовут", self.name)
        print("Мне", self.age_2, "лет")

person_1 = Person("Mikle")
person_1.Info()
del person_1
person_2 = Person("Никита")
person_2.Info()

# Статический метод
class River:
    @staticmethod
    def get_class_details():
        print("Это класс River")

class Car(River):
    def staticmethod(self):
        print("Это класс Car")


my_dream = River
my_dream.get_class_details()
my_dream_1 = Car
my_dream_1.staticmethod("BMW")

River.get_class_details()






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
    def staticmethod():
        print("Это класс River")

class Car(River):
    def get_class_details(self):
        print("Это класс Car")


my_dream = River
my_dream.staticmethod()
my_dream_1 = Car
my_dream_1.get_class_details("Audi A8")

River.staticmethod()

# Class Method

class MyFuture():
    TOTAL_OBJECTS = -1

    def __init__(self):
        MyFuture.TOTAL_OBJECTS = MyFuture.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)


class ChildClass(MyFuture):
    def __init__(self):
        ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS + 1

    pass

# Создаем объекты
my_obj1 = ChildClass()
my_obj2 = MyFuture()
my_obj3 = MyFuture()
# Вызываем classmethod
ChildClass.total_objects()
MyFuture.total_objects()








# Методы Класса

# class MyClass():
#     @staticmethod
#     def staticmethod():
#         print('static method called')

# class children_My_class(MyClass):
#     pass
# my_obj = MyClass()
# my_obj.staticmethod()
# my_obj_1=children_My_class()
# my_obj_1.staticmethod()

# class Person():
#     @staticmethod
#     def is_adult(age):
#         if age > 18:
#             return True
#         else:
#             return False

# print(Person.is_adult(15))

class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

# Создаём объекты
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()

#Вызываем classmethod
MyClass.total_objects()










# class Calc:

#     def __init__(self):
      #   self.vvod()

#    def plus(self):
        # return self.a + self.b
  #   def minus(self):
   #      return self.a - self.b
    # def dele(self):
      #   if self.b==0:
        #     return "error"
        # else:
        #     return self.a / self.b
    # def umn(self):
    #     return self.a * self.b
    # def vvod(self):
      #   self.a=int(input("Введите первое число: "))
        # self.b=int(input("Введите второе число: "))

# while True:
  #   ex = Calc()
    # c = input("Введите операцию(+,*,/,-): ")

    # if c=='+':
      #   print(ex.plus())
    # elif c=="-":
      #   print(ex.minus())
    # elif c=='*':
      #   print(ex.umn())
    # elif c=='0':
      #   break
    # else:
      #   print(ex.dele())

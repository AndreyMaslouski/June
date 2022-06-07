# class Rectangle:
#     def __init__(self,width,height):
#         self._width=width
#         self._height=height

#     def get_width(self):
#         return self._width

#     def set_width(self,w):
#         self._width = w

#     def get_height(self):
#         return self._height

#     def set_height(self,h):
#         self._height = h

#     def area(self):
#         return self._width*self._height

# rect=Rectangle(10,20)
# rect.get_width()
# rect._width

# Модифицируем наш класс Rectangle:
class Rectangle:

    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self,w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self,h):
        self.__height = h

    def area(self):
        return self.__width*self.__height

# Попытка обратиться к __width напрямую вызовет ошибку, нужно
# работать только через get_width():

rect = Rectangle(10,20)
# rect._width
rect.get_width()

# Но на самом деле это сделать можно, просто этот атрибут
# теперь для внешнего использования носит название:
# _Rectangle__width:

rect._Rectangle__width
# Результат:10
rect._Rectangle__width = 20
rect.get_width()
# Результат: 20

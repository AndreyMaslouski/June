# Полиморфизм.
# Добавим в наш базовый класс метод info(), который печатает
# сводную информацию по объекту класса Figure и переопределим этот
# метод в классе Rectangle, добавим в него дополнительные данные:
class Figure:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print("Figure")
        print("Color: " + self.__color)

# Продемонстрируйте разные уровни доступа на примере любого класса

class Example:
    def __init__(self,tea,coffee,area):           # __init__ private level
        self.__tea = tea
        self.__coffee = coffee               # private
        self.__area = area
    def get_tea(self):
        return self.__tea                    # private

    def set_tea(self,t):
        self.__tea = t                      # private

    def get_coffee(self):
        return self.__coffee

    def set_coffee(self,c):
        self.__coffee = c

    def area(self):
        return self.__tea*self.__coffee*self.__area


Rect = Example(7,11,25)
print(Rect._Example__tea)              # Вывод private
print(Rect._Example__coffee)           # Вывод private
print(Rect._Example__area)             # Вывод private
print(Rect.get_tea())                  # Вывод public
print(Rect.area())                     # Вывод public
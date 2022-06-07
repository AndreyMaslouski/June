# Продемонстрируйте разные уровни доступа на примере любого класса

class Example:
    def __init__(self,tea,coffee,area,tea_1,coffee_1):      # __init__ private level
        self._coffee = coffee_1
        self._tea = tea_1
        self.__tea = tea
        self.__coffee = coffee            # private
        self.__area = area
    def get_tea(self):
        return self.__tea                 # private

    def main_team(self):
        return self._tea                  # protected

    def set_tea(self,t):
        self.__tea = t                    # private

    def get_coffee(self):
        return self.__coffee             # private

    def coffee_team(self):
        return self._coffee               #protected

    def set_coffee(self,c):
        self.__coffee = c                 # private

    def area(self):
        return self.__tea*self.__coffee*self.__area


Rect = Example(7,11,25,29,35)
print(Rect._Example__tea)              # Вывод private
print(Rect._Example__coffee)           # Вывод private
print(Rect._Example__area)             # Вывод private

print(Rect.get_tea())                  # Вывод public
print(Rect.area())                     # Вывод public
print(Rect.main_team())                # Вывод public

print(Rect._tea)                       # Вывод protected
print(Rect._coffee)                    # Вывод protected

# Продемонстрируйте разные уровни доступа на примере любого класса

class Example:
    def __init__(self,tea,coffee):           # __init__ private level
        self.__tea = tea
        self.__coffee = coffee               # private

    def get_tea(self):                       # protected
        return self.__tea                    # private

    def set_tea(self,t):                    # protected
        self.__tea = t                      # private

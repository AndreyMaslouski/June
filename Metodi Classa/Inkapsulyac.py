# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model
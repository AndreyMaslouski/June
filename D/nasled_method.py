# Практическое занятие
# В предыдущем задании допишите:
# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price. 3. Свои начальные
# значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом
# данной скидки.
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов
# данный метод принимает объект дома и его цену.
# 2. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и
# совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка
# на дом и размер скидки.

class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f"Вы заработали {amount}. У Вас {self.__money} денег")


# 1.1
class House:
    # 1.2,1.3
    def __init__(self, area, price):
        self._area = area
        self._price = price

    # 1.4
    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price

# 2.1
class SmallHouse(House):
    default_area = 40

    # 2.2
    def __init__(self, price):
        super.__init__(SmallHouse.default_area, price)




if __name__ == '__main__':
    Human.default_info()
    Alex = Human('Alex', 25)
    Alex.info()
    Alex.earn_money(10000)
    Alex.earn_money(5000)
    Alex.info()

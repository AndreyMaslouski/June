# Класс Human
# 1. Создайте класс Human
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два
# параметра: name и age. Для этих параметров задайте значения по
# умолчанию, используя свойства default_name и default_age. В методе
# __init__() определите четыре свойства: Публичные - name и age. Приватные
# - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name,
# age, house и money.
# 5. Реализуйте справочный статический метод default_info(), который будет
# выводить статические поля default_name и default_age.
# 6. Реализуйте метод earn_money(), увеличивающий значение свойства mone
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
#3.1

    def __make_deal(self,house,price):
        self.__money -= price
        self.__house = house



if __name__ == '__main__':
    Human.default_info()
    Alex = Human('Alex', 25)
    Alex.info()
    Alex.earn_money(10000)
    Alex.earn_money(5000)
    Alex.info()

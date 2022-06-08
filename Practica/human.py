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
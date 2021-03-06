# Домашнее задание
# Класс Alphabet
#
# 1.1 Создайте класс Alphabet
#
# 1.2 Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
#
# 1.3 Создайте метод print(), который выведет в консоль буквы алфавита
#
# 1.4 Создайте метод letters_num(), который вернет количество букв в алфавите

# Класс EngAlphabet
#
# 2.1 Создайте класс EngAlphabet путем наследования от класса Alphabet
#
# 2.2 Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве параметров
# ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться
# свойством ascii_uppercase из модуля string).
#
# 2.3 Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.

# 2.4 Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта
# буква к английскому алфавиту.
#
# 2.5 Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
#
# 2.6 Создайте статический метод example(), который будет возвращать пример текста на английском языке

# Тесты:
#
# 1. Создайте объект класса EngAlphabet
#
# 2. Напечатайте буквы алфавита для этого объекта
#
# 3. Выведите количество букв в алфавите
#
# 4. Проверьте, относится ли буква F к английскому алфавиту
#
# 5. Проверьте, относится ли буква Щ к английскому алфавиту

# 6. Выведите пример текста на английском языке

# 1.1,1.2
import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    # 1.3
    def print(self):
        print(self.letters)

    # 1.4
    def letters_num(self):
        return len(self.letters)


# 2.1, 2.2, 2.3
class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('lang', string.ascii_uppercase)
        self.__letters_num = __letters_num = 26

    # 2.4
    def is_en_letter(self, letter):
        if letter in string.ascii_uppercase:
            print(f'Буква {letter} относится к англ.алфавиту')
        else:
            print(f'Буква {letter} не относится к англ.алфавиту')

    # 2.5
    def letters_num(self):
        print(self.__letters_num)

    # 2.6
    @staticmethod
    def example():
        return ('Good and Sunny Day!')


# Тесты
if __name__ == '__main__':
    ex = EngAlphabet()
    ex.print()
    ex.letters_num()
    print(ex.is_en_letter('F'))
    print(ex.is_en_letter('Щ'))
    print(ex.example())

# 1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
#
# Поле
#
# Тип, описание
#
# book_id
#
# INT PRIMARY KEY AUTO_INCREMENT
#
# title
#
# VARCHAR(50)
#
# author
#
# VARCHAR(30)
#
# price
#
# DECIMAL(8, 2)
#
# amount
#
# INT
#
# 2.Занесите новую строку в таблицуbook
#
# 3.Выбрать информацию о всех книгах из таблицы book.


import sqlite3

#1 Создаём Таблицу book:
base = sqlite3.connect('book.db')
cursor = base.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS data(login,password)'.format('data'))
base.commit()

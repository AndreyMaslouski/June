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
# 2.Занесите новую строку в таблицу book
#
# 3.Выбрать информацию о всех книгах из таблицы book.


import sqlite3
from nasled_method import Human

#1 Создаём Таблицу book:
base = sqlite3.connect('book.db')
cur = base.cursor()



base.execute('CREATE TABLE IF NOT EXISTS data(login PRIMARY KEY,password text)'.format('data'))
base.commit()

# cur.execute('INSERT INTO data VALUES(?,?)',('jonny 123','123456789'))
# base.commit()
# cur.execute('INSERT INTO data VALUES(?,?)',('billy123','password'))
# base.commit()
cur.execute('INSERT INTO data VALUES(?,?)',('jonny 123','123456789'))
base.commit()
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

#1 Создаём Таблицу book:
base = sqlite3.connect('book.db')
cur = base.cursor()

# base.execute('CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,title VARCHAR(50),''author VARCHAR(30),price DECIMAL(8,2), amount INT)'.format('book'))
# base.commit()

# r = cur.execute('SELECT*FROM book').fetchall()
# print(r)
# base.commit()

#2
# base.execute('INSERT INTO BOOK(book_id,title,author,price,amount) VALUES(17,"Молодая Гвардия",15,7,555)')
# base.commit()
#3
r = cur.execute('SELECT*FROM book').fetchall()
print(r)
base.commit()
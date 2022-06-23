# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то
# удалите четвёртую запись БД

import sqlite3
import random


conn = sqlite3.connect('z_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,
col_2 INTEGER) ''')


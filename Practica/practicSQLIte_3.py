# Создайте метод класса для работы с БД
# В БД
# 1. Если передан 1 аргумент, вставить в таблицу запись с числом 3
# 2. Если переданы 2 аргумента: проверить или второй аргумент является
# числом.
# 3. Если условие верно, то удалить первую запись с БД
# 4. Если переданы 2 аргумента, их значения не известны, а 3 является
# числом, то обновить на число 77 запись 3.

import sqlite3
import random


conn = sqlite3.connect('z_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)


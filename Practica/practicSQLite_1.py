import sqlite3

# Создайте новую Базу данных
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое
# число
# Число запрашивается с клавиатуры, а слова задаются статически.
# Выведите каждую запись в отдельную строку

conn = sqlite3.connect("z_1.db")
cursor = conn.cursor()
a = int(input())
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT, col_3 INTEGER) ''')
cursor.execute('''INSERT into tab_1(col_1,col_2,col_3) VALUES('hello','world',?)''',(a,))
conn.commit()
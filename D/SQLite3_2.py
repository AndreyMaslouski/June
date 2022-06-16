import sqlite3

# Создать 2 таблицы в Базе Данных
#
# Одна будет хранить текстовые данные(1 колонка)
#
# Другая числовые(1 колонка)
#
# Есть список, состоящий из чисел и слов.
#
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
#
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во вторую таблицу слово: «нечётное»
#
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше, то обновить 1 запись в первой таблице на «hello»


#1 Создаём Таблицы:
base = sqlite3.connect('text.db')
cursor = base.cursor()

# создаем таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 VARCHAR(50))''')
base.commit() # сохраняем изменения

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
base.commit() # сохраняем изменения

#2
a = [15,27,'world',8,16,'sunny',26,14,'sky',35,44]

for i in a:
    if type(i) == str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (i,))
        d = len(i)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (d,))
        base.commit()

        k = cursor.fetchall()

        if len(k) > 5:
            cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
            base.commit()
        else:
            cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = ?''', (1,))
            base.commit()
    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (i,))
            base.commit()
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES ('nechetnoe')''')
            base.commit()

# cursor.execute('''DROP TABLE tab_1''')
# cursor.execute('''DROP TABLE tab_2''')

cursor.execute('''SELECT*FROM tab_2''')
k2 = cursor.fetchall()
print(k2)

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)




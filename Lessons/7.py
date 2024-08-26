#database - база данных
#python - регистрозавимий видит большие буквы print()  и Print
# SQL - язык структуированных запросов, работает с табличными relation (no relation - не табличные)
# noSQL - язык
# framework для SQL - СУБД (система управления баз данных)

# Oracle - СУБД майкрософта
# SQlite, PosgreSQL, mongoDB

# SQlite3

# база данных должна лежать на сервере

import sqlite3 as sql3
# # принципы работы (одна функия)
# db = sql3.connect('user.db')
# cursor = db.cursor()
# #cursor - отец всех методов
# with автоматом открывает, сохраняет и закрывает файл

with sql3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    fulname TEXT NOT NULL,
    pol INT DEFAULT 0,
    bdate DATE
    ) ''')

# CREATE
#     cursor.execute('''INSERT INTO students (fulname, pol, bdate)
#     VALUES ('beka', 1, '2020-01-01'), ('alina', 2, '2020-12-31')
#     ''')
#   read
    cursor.execute('''SELECT rowid,* FROM students''')
    # print(cursor.fetchall())
    for row in cursor.fetchall():
        print(row)   # это для табличного вида

# Py не может на прямую обратиться к базе данных, поэтому при execute можно писать на другом языке SQL
# NOT NULL - ограничитель это поле не должнр быть пустым
# DEFAULT - по умолчанию тоже ограничитель
# fetchone - достает первые данные
# fetchall - все данные
# fetchmany(3) - количество сколько достать
# CRUD - create, read, update, delete


#сохранить результат - db.commit()
#закрыть файл чтобы другие могли пользоваться - db.close()
# эти две команды прописываются в конце после каждого изменения




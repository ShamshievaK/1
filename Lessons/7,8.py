#database - база данных
#python - регистрозавимий видит большие буквы print()  и Print
# SQL - язык структуированных запросов, работает с табличными relation (no relation - не табличные)
# noSQL - язык
# framework для SQL - СУБД (система управления баз данных)

# Oracle - СУБД майкрософта
# SQlite, PosgreSQL, mongoDB

# SQlite3

# база данных должна лежать на сервере

# import sqlite3 as sql3
# # # принципы работы (одна функия), Sqlite3 - позволяет создать файл в базе данных
# # db = sql3.connect('user.db')
# # cursor = db.cursor()
# # #cursor - отец всех методов
# # with автоматом открывает, сохраняет и закрывает файл
#
# with sql3.connect('users.db') as connection:
#     cursor = connection.cursor()
#
#     cursor.execute('''CREATE TABLE IF NOT EXISTS students (
#     fulname TEXT NOT NULL,
#     pol INT DEFAULT 0,
#     bdate DATE
#     ) ''')
#
# # CREATE
# #     cursor.execute('''INSERT INTO students (fulname, pol, bdate)
# #     VALUES ('beka', 1, '2020-01-01'), ('alina', 2, '2020-12-31')
# #     ''')
# #   read
#     cursor.execute('''SELECT rowid,* FROM students''')
#     # print(cursor.fetchall())
#     for row in cursor.fetchall():
#         print(row)   # это для табличного вида

# Py не может на прямую обратиться к базе данных, поэтому при execute можно писать на другом языке SQL
# NOT NULL - ограничитель это поле не должнр быть пустым
# DEFAULT - по умолчанию тоже ограничитель
# fetchone - достает первые данные
# fetchall - все данные
# fetchmany(3) - количество сколько достать
# VARCHAR - ограничитель длина текста
# CRUD - create, read, update, delete
# AUTOINREMENT увеличивает число на 1

#сохранить результат - db.commit()
#закрыть файл чтобы другие могли пользоваться - db.close()
# эти две команды прописываются в конце после каждого изменения

import sqlite3
with sqlite3.connect('game.db') as connection:
    cursor = connection.cursor()
# Удаляем таблтицу через  DROP
#     cursor.execute('''DROP TABLE IF EXISTS users''')
# связи в табл бывают один к одному, один ко множеству и множество к множеству

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT VARCHAR(55) NOT NULL,
    nickname TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT NOT NULL,
    users_id INTEGER,
    FOREIGN KEY(users_id) REFERENCES users(id)
    )''')
    # cursor.execute('''INSERT INTO users (name, nickname)
    # VALUES ('beka', 'ECLIPSE'), ('kani', 'ZODIAC')''')

    cursor.execute('''SELECT * FROM users''')
    for row in cursor.fetchall():
        print(row)

    # cursor.execute('''INSERT INTO games (game_name, users_id)
    # VALUES ('LOL', 2), ('LOL', 2)''')
    #
    # cursor.execute('''SELECT * FROM games''')
    # for row in cursor.fetchall():
    #     print(row)

# ORDER BY id - сортируй если добавить DESC - сортирует наоборот, LIMIT-сколько лимит вводим цифру:
# cursor.execute('''SELECT * FROM users WHERE id>1 ORDER BY id DESC LIMIT 1''')
# JOIN - обьединяет 2 табл (2 вида ЛЕФТ(покажет прошлые данные но с NONE) и РАЙТ(обычный JOIN если удалить то удалит))
# LEFT JOIN
    cursor.execute('''SELECT users.nickname, games.game_name
    FROM users
    JOIN games ON users.id = games.users_id
    ''')
    for row in cursor.fetchall():
        print(row)

    # cursor.execute('''DELETE FROM users WHERE id = 1''')

    cursor.execute('''SELECT * from users''')
    for row in cursor.fetchall():
        print(row)

    cursor.execute('''UPDATE users SET nickname = "beka" WHERE id=1''')
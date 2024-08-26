import sqlite3 as sql3
from pyclbr import readmodule

with sql3.connect('user.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    fullname TEXT NOT NULL,
    salary INT DEFAULT NULL
    )''')

    cursor.execute('''INSERT INTO employees (fullname, salary)
   VALUES ('Жанышев В Б', '20000'), ('Федорова Е П', '45000')
   ''')

    cursor.execute('''SELECT rowid, * FROM employees''')
    for row in cursor.fetchall():
        print(row)
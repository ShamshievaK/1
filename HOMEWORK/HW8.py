import sqlite3

with sqlite3.connect('person.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
    DepartmentId INTEGER PRIMARY KEY AUTOINCREMENT,
    DepartmentName TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    EmployeeId INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentId INTEGER,
    FOREIGN KEY (DepartmentId) REFERENCES departments(DepartmentId)
    )''')

    # cursor.execute('''INSERT INTO departments (DepartmentName)
    # VALUES ('101:HR')
    # ''')
    # cursor.execute('''INSERT INTO departments (DepartmentName)
    # VALUES ('102:IT')
    # ''')
    # cursor.execute('''INSERT INTO departments (DepartmentName)
    # VALUES ('103:Sales')
    # ''')
    #
    # cursor.execute('''INSERT INTO employees (FirstName, LastName, DepartmentId)
    # VALUES ('Kani', 'Shamshieva', 102), ('Oksana', 'Petrova', 101), ('Dasha', 'Smirnova', 102), ('Tatyna', 'Melisova', 101), ('Tomiris', 'Semeeva', 103), ('Bema', 'Aibekova', 103)''')
    # cursor.execute('''SELECT * FROM employees''')
    # for row in cursor.fetchall():
    #     print(row)

    cursor.execute('''SELECT employees.FirstName, employees.LastName, departments.DepartmentId
    FROM employees
    JOIN departments ON employees.DepartmentId = departments.DepartmentId
        ''')
    # for row in cursor.fetchall():
    #     print(row)

    cursor.execute('''SELECT FirstName, LastName FROM employees WHERE DepartmentId=102''')
    for row in cursor.fetchall():
        print(row)
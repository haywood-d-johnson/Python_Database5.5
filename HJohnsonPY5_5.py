"""
@author: Haywood D. Johnson
@class: ITSE 2359 Advanced Computer Programming
@assignment: Assignment 5.5 Python – Database
"""

import sqlite3 as sl

con = sl.connect("my-test.db")

c = con.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USER' ''')

if c.fetchone()[0]==1 :
    print("Table exists.")
else :
    print("Table does not exist.")

    with con:
        con.execute("""
            CREATE TABLE USER ( 
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """)

    sql = "INSERT INTO USER (id, name, age) VALUES(?, ?, ?)"
    data = [
        (1, "ALICE", 21),
        (2, "BOB", 22),
        (3, "CHRIS", 23)
    ]

    with con:
        con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)
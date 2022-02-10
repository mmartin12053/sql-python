import sqlite3
from datetime import date

def go():
    F_name = input("what is your first name:\n")
    L_name = input("what is your last name:\n")
    user_email = input("what is your Email:\n")
    t = date.today()

    print(F_name)
    print(L_name)
    print(user_email)
    print(t)
    

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS testTable(first_name TEXT, last_name TEXT, user_email TEXT, timestamp TEXT)')

    def data_entry():
        c.execute(f'INSERT INTO testTable VALUES("{F_name}", "{L_name}", "{user_email}", "{t}")')
        conn.commit()
        c.close()
        conn.close()



    create_table()
    data_entry()

    go()

go()
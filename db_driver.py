import sqlite3

class DB_class:
    conn = None
    cursor = None

    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()
        cmd = 'CREATE TABLE IF NOT EXISTS products (name TEXT, description TEXT)'
        self.cursor.execute(cmd)

        cmd = 'CREATE TABLE IF NOT EXISTS history (user TEXT, request TEXT)'
        self.cursor.execute(cmd)

        cmd = 'CREATE TABLE IF NOT EXISTS users (user TEXT, passwd TEXT)'
        self.cursor.execute(cmd)

    def insert_users(self, user, passwd):
        cmd = 'INSERT INTO users VALUES (\'%s\', \'%s\')' % (user, passwd)
        print(cmd)
        self.cursor.execute(cmd)
        self.conn.commit()

    def get_users(self):
        cmd = 'SELECT * FROM users'
        self.cursor.execute(cmd)
        res = self.cursor.fetchall()
        print(res)


my_db = DB_class()
my_db.insert_users('user1', '111111')
my_db.get_users()

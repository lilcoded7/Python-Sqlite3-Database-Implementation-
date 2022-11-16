# implementation of sqlite3  in python 

# importing sqlite3
import sqlite3





class Database:

    
    
    def __init__(self):
        self.con = sqlite3.connect('employees.db')
        self.cur = self.con.cursor()
        self.create_table()
        


    #   CREATING TABLE FOR USER METHOD
    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT , username , email TEXT, password TEXT, date TEXT)''')
        self.con.commit()

    #   INSERTING INTO TABLE METHOD
    def insert(self, items):
        self.cur.execute(''' INSERT OR IGNORE INTO  employee VALUES(?,?,?,?,?)''', items)
        self.con.commit()
        

    #   FETCHING FROM DATABASE METHOD
    def read(self):
        self.cur.execute('''SELECT * FROM employee''')
        rows = self.cur.fetchall()
        return rows

    #   DELETING USER FROM THE DATABASE 
    def delete(self, username):
        self.cur.execute('DELETE FROM employee WHERE username = ?', username)
        self.con.commit()
        

    #   UPDATE METHOD 
    def update(self, email,id):
        self.cur.execute("UPDATE employee SET username = ? WHERE id = ? ", (email, id))
        self.con.commit()
        self.con.close()
    
    

        

# db = Database()



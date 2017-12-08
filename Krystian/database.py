import sqlite3

    
with sqlite3.connect("database.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR(20) NOT NULL,
transactions VARCHAR(20))
''')

cursor.execute("""INSERT INTO users(username, transactions) VALUES("Krystian", "none")""")
cursor.execute("""INSERT INTO users(username, transactions) VALUES("Sølve", "none")""")
db.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
       
        


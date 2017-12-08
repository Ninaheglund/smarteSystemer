import sqlite3,time
import facerec


def login():
    while True:
        user_id = facerec.Facerec()
        #username = raw_input("Please enter your username: ")
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM users WHERE ID = ?")
        cursor.execute(find_user,[(user_id)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[1])
                
            #return("Exit")
            print(user_id)
            return user_id
        else:
            print("User not found")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("Exit")
                break


def newUser():
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE username = ?")
        cursor.execute(findUser, [(username)])

        if cursor.fetchall():
            print("Username Taken, please try again")

        else:
                found = 1
                
    insertData = '''INSERT INTO users(username) VALUES(?)'''
    cursor.execute(insertData, [(username)])
    db.commit()

def menu():
    while True:
        print("Welcome to my system ")
        menu =('''
        1 - Create New User
        2 - Login to system
        3 - Exit system\n''')

        userChoice = input(menu)

        if userChoice == "1":
            newUser()

        elif userChoice == "2":
            user = login()
            print(user)
            return user
            
        elif userChoice == "3":
            break

        else:
            print("Command not recognized: ")
                      

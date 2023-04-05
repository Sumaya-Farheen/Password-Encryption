#!/usr/bin/pyton

import bcrypt 
def welcome():
    print("welcome to your dashboard")

def gainAccess (username = None, password = None):
    print("Enter your name: ", username)
    print("Enter your password", password)

    if not len(username or password) < 1:
        if True:
            db = open('C:\Seltam\ML\db.txt', "r")
            d = []
            f = []

            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d,f))
            try:
                if username in data:
                    hashed = data[username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(password.encode(), hashed):
                            print("Login success!")
                            print("Hi", username)
                            welcome()
                        else:
                            print("Incorrect passwords or username")

                    except:
                        print('Incorrect passwords or username')

                else:
                    print("username doesn't exist")

            except:
                print("password or username doesn't exist")
        else:
            print("Error logging into the system")
                
    else:
                        
        print("Please attempt login again")
        gainAccess()

        #b = b.strip()
        #accessDB

def register(username = None, password1 = None, password2 = None ):
    print(input("Enter a username:", username))
    print(input("Create password", password1))
    print(input("Confirm password", password2))

    db = open('C:\Seltam\ML\db.txt', "r")
    d = []
    for i in db:
        a,b = i.split(" , ")
        b = b.strip()
        c = a, b 
        d.append(a)
    if not len(password1) <=8:
        db = open('C:\Seltam\ML\db.txt', "r") 
        d = []
        for i in db:
            a,b = i.split()
            b = b.strip()
            c = a,b
            d.append(a)
            if not len(password1) <=8:
                db = open('C:\Seltam\ML\db.txt', "r")
                if not username == None:
                    if len(username) <1:
                        print("Please provide a username")
                        register()
                    elif(username) in d:
                        print("username exists")
                        register()
                    else:
                        if password1 == password2:
                            password1 == password1.encode('utf-8')
                            password1 = bcrypt.hashpw (password1, bcrypt.gensalt())

                            db = open('C:\Seltam\ML\db.txt', "a")
                            db.write(username+"," + str(password1)+"\n")
                            print("user created sucessfully!")
                            print("Please login to proceed:")
                            # print("Please login to proceed:")
                            print("texts")

                        else:
                            print("Passwords do not match")
                            register()
                else:
                    print("Password too short")

def home(option=None):
    print("Welcome, please select an option")
    option = input(" Login | Signup")
    if option == "Login":
        gainAccess()
    elif option == "Signup":
        register()
    else:
        print("Please enter a valid parameter")

home()







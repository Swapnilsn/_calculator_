#Write a program to login  using file handling  
def Register():
    print("Hello! You need to register an account before you can begin")
    username = input("Please enter a username: ")
    password = input("Now please enter a password: ")
    file = open("login.txt","a")
    file.write (username)
    file.write (",")
    file.write (password)
    file.write("\n")
    file.close()
    print ("Your login details have been saved. ")
    print("You will now need to login")
    Login() 

def Login():
    print("Please enter your details to log in")
    username1 = input("Please enter your username: ")
    password1 = input("Please enter your password: ")

    file = open("login.txt","r")

    for row in file:
        field = row.split(",")
        username = field[0]
        password = field[1]
        lastchar = len(password)-1
        password = password[0:lastchar]
        print(username,password)
        

        if username1 == username and password1 == password:
            print("Hello",username)
        else:
            print("incorrect")

user=input("Are you already a user? ")

if user=="Yes":
  Login()

else:
 user =="No"
 Register()


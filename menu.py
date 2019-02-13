import os
import hashlib
from random import randint
import csv

def line_break(args):
    lineBreak = "+"
    for i in range(len(args)):
        lineBreak += '-'.center(args[i], '-') + "+"
    #  lineBreak = "+" + '−'.center(len1, '−') + "+" + '−'.center(len2, '−') + "+"
    return lineBreak

def normal(args, length):
#    print(args, length)
    normal = "|"
    for i in range(len(args)):
        normal += args[i].center(length[i], ' ') + "|"
    return normal

def create_menu():
    length = (14, 35)
    print(line_break(length))
    print(normal(("Press 1 to", "Choose file"), length))
    print(normal(("Press 2 to", "Create new user in file"), length))
    print(normal(("Press 3 to", "Show the content of the file"), length))
    print(normal(("Press 4 to", "Create new windows/linux users"), length))
    print(normal(("Press 5 to", "Exit the program"), length))
    print(line_break(length))

def create_user(csv_file):
    choice = "yes"
    length = (12, 14, 30, 66, 25, 20)
    while (choice == "y" or choice == "yes"):
        first_name = input("firstname: ")
        last_name = input("lastname: ")
        email = input("email: ")
        password = hashlib.sha1(input("password: ").encode('utf-8')).hexdigest()
        department = input("department: ")
        username = first_name[0] + last_name + str(randint(0, 10))
        with open(csv_file, 'a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([first_name, last_name, email, password, department, username])
        line_break(length)
        normal([first_name, last_name, email, password, department, username], length)
        line_break(length)
        choice = input("Create another user? write y/yes to create another: ")

def show_content(csv_file):
    length = (12, 14, 30, 66, 25, 20)
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)

        print(line_break(length))
        print(normal(("First Name", "Last Name", "Email", "Password", "Department", "Username"), length))
        print(line_break(length))
        for row in reader:
            theRow = row["first_name"], row["last_name"], row["email"], row["pass"], row["department"], row["username"]
            print(normal(theRow, length))
        print(line_break(length))

def main():
    csv_file = False
    
    while True:
        create_menu()

        try:
            menu = int(input())
        except:
            print("Not a valid choice")
            pass

        if menu == 1:
            csv_file = input("Write filename or full path: ")
            # if not csv_file.exists():
            #     print("That file does not exist")
            #     csv_file = ""
        elif menu == 2:
            if csv_file:
                create_user(csv_file)
            else:
                print("Either you have not set a csv file or the csv file you have chosen does not exist!")

        elif menu == 3:
            # if csv_file.exists():
            if csv_file:
                show_content(csv_file)
            else:
                print("Either you have not set a csv file or the csv file you have chosen does not exist!")

        elif menu == 4:
            ...
        elif menu == 5:
            break
        else:
            print("Not a valid number!!!")

main()

import os
import csv

# def length_args(arg1, arg2):
#     len1 = len(max(arg1, key=len)) + 6
#     len2 = len(max(arg2, key=len)) + 6
#     return len1, len2
# 
def line_break(*args):
    lineBreak = "+"
    for i in args:
        lineBreak += '-'.center(i, '-') + "+"
    #  lineBreak = "+" + '−'.center(len1, '−') + "+" + '−'.center(len2, '−') + "+"
    return lineBreak

def normal():
    normal = "|" + arg1.center(len1, ' ') + "|" + arg2.center(len2, ' ') + "|"
    return normal

def create_menu():
    print(line_break(14, 35))
    print(normal("Press 1 to", "Choose file", 14, 35))
    print(normal("Press 2 to", "Create new user in file", 14, 35))
    print(normal("Press 3 to", "Show the content of the file", 14, 35))
    print(normal("Press 4 to", "Create new windows/linux users", 14, 35))
    print(normal("Press 5 to", "Exit the program", 14, 35))
    print(line_break(14, 35))


def main():
    while True:
        create_menu()
        menu = int(input())
        if menu == 1:
            csv_file = input("Write filename or full path")
            # if not csv_file.exists():
            #     print("That file does not exist")
            #     csv_file = ""
        elif menu == 2:
            ...
        elif menu == 3:
            length = 12, 12, 25, 40, 25, 20
            # if csv_file.exists():
            if True:
                with open(csv_file, newline='') as file:
                    reader = csv.DictReader(file)
                    print(line_break(len0, len1, len2, len3, len4, len5))

                    for row in reader:
                        ...



          #  print(line_break(z, x))
          #  print(normal(title[0], title[1], z, x))
          #  print(line_break(z, x))
          #  print(normal(a[0], b[0], z, x))
          #  print(normal(a[1], b[1], z, x))
          #  print(line_break(z, x))
          #  men = input()
        elif menu == 4:
            ...
        elif menu == 5:
            break
        else:
            print("Not a valid number!!!")

main()

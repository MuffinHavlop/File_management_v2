import time
import random
import os

for i in range(1, 4):
    time.sleep(1)
    os.system('cls')
    print("loading", "."*i)

print("***FILE MANAGING SYSTEM***")
diretory = "C:/System/System32/Windows"
command_list = ["remove", "move", "write"]

def Find_file():
    global Target
    print("Select a target File")
    diretory = "C:/System/System32/Windows"
    Target = input(f"{diretory}: ")
    try:
        os.remove(f"D:\code\python\ilemanagementtest\ilemangementv2\ilelist\{Target}")
        print(f"{Target} has been succesfully deleted!!!")
    except FileNotFoundError:
        print(f"{Target} does not exists")

def Find_edit_file():
    global File_name
    global content
    diretory = "C:/System/System32/Windows"
    File_name= input(f"{diretory}: ")
    content = input("Enter content(Optional): ")
    try:
        with open(f"D:\code\python\ilemanagementtest\ilemangementv2\ilelist\{File_name}", "w") as file: 
            file.write(content)
            print(f"{File_name} has been succesfully edited!")
    except FileNotFoundError:
        print(f"{File_name} does not exists")

while True: 
    print("What do you wish to do?:")
    Command = input("Command: ")
    if Command not in command_list:
        print("Error, unknown command")
    else:
        if Command == "remove":
            Find_file()
        elif Command == "move":
            print("this function can't work yet!!")
            pass
        else:
            Find_edit_file()    

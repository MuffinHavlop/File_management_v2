import time
import random
import os

for i in range(1, 4):
    time.sleep(1)
    os.system('cls')
    print("loading", "."*i)

print("***FILE MANAGING SYSTEM***")
diretory = "C:/System/System32/Windows"
command_list = ["remove", "move", "add"]

def Find_file():
    global Target
    print("Select a target File")
    diretory = "C:/System/System32/Windows"
    Target = input(f"{diretory}: ")
    try:
        os.remove(f"D://code//python//filemanagementtest//{Target}")
        print(f"{Target} has been succesfully removed!")
    except FileNotFoundError:
        print(f"{Target} does not exists")
   
while True: 
    print("What do you wish to do?:")
    Command = input("Command: ")
    if Command not in command_list:
        print("Error, unknown command")
    else:
        if Command == "remove":
            Check = False
            while Check == False:
                Find_file()
            os.remove(Target)
        elif Command == "move":
            pass
        else:
            try:
                File_name = input("Enter the new text file name here: ")
                content = input("Enter content(Optional): ")
                with open(File_name, "w") as file: 
                    file.write(content)
                print(f"'{File_name} has been created succesfully'")
            except FileExistsError:
                print(f"The file {File_name} already exists")
                

            
    

    
    
    

        

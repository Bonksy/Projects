# Project: A Command Line Todo List

# Constants

ADD = "add"
QUIT = "quit"
SHOW_ALL = "show all"
DELETE = "delete"


# Menu Functions

def menu():
    print("------------------------")
    print("1: Add to todo list")
    print("2: Mark task as complete")
    print("3: Delete from todo list")
    print("4: Show todo list (enter 'Show all')")
    print("5: Quit")
    print("------------------------")



todo_list = []

while True:

    menu()
    
    command = input("What do you want to do?: " )

    
    todo_list.append(item)

    if command == ADD.lower():
        item = input("Please enter task to add to your list: ")
        print(f"Task '{item}' has been added to your to do list")

    elif command == SHOW_ALL.lower():
        print("Todo List:")
        for i, item in enumerate(todo_list, start = 1):
            print(f"{i}.", item)
            continue
    
    elif command == QUIT.lower():
        print("Quitting todo list")
        print("Goodbye!")
        break
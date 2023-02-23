# Project: A Command Line Todo List

# Constants

ADD = "add"
COMPLETE = "complete"
SHOW_COMPLETE = "show complete"
QUIT = "quit"
SHOW_ALL = "show all"
DELETE = "delete"


# Menu Functions

def menu():
    print("------------------------")
    print("1: Add to todo list")
    print("2: Mark task as complete")
    print("3: Show complete list")
    print("4: Delete from todo list")
    print("5: Show todo list (enter 'Show all')")
    print("6: Quit")
    print("------------------------")

# Empty lists

todo_list = []
complete_list = []


while True:

    menu()
    
    command = input("What do you want to do?: " )

    if command == ADD.lower():
        item = input("Please enter task to add to your list: ")
        todo_list.append(item)
        print(f"Task '{item}' has been added to your to do list")
        continue

    elif command == COMPLETE.lower():
        print("Todo List:")
        for i, task in enumerate(todo_list, start = 1):
            print(f"{i}.", task)
        task_num = int(input("Which task number do you want to mark as complete? "))   
        if task_num < 1 or task_num > len(todo_list):
            print("Invalid number")
        else:
            complete_list.append(todo_list[task_num - 1])
            print(f"Task {task_num} {todo_list[task_num - 1]} has been marked as complete.")
            todo_list.pop(task_num - 1)

    elif command == SHOW_COMPLETE.lower():
        print("Completed Tasks")
        for i, item in enumerate(complete_list, start = 1):
            print(f"{i}.", item)

    elif command == DELETE.lower():
        print("Todo list:" )
        for i, task in enumerate(todo_list, start = 1):
            print(f"{i}.", task)
        del_task = int(input("Which task number do you want to delete? "))
        print(f"Task {del_task} {todo_list[del_task - 1]} has been deleted from the list.")
        todo_list.pop(del_task - 1)
        for i, task in enumerate(todo_list, start = 1):
            print(f"{i}.", task)
        


    elif command == SHOW_ALL.lower():
        print("Todo List:")
        for i, item in enumerate(todo_list, start = 1):
            print(f"{i}.", item)
            continue
    
    elif command == QUIT.lower():
        print("Quitting todo list")
        print("Goodbye!")
        break
shopping_list = []

#Functions
def add_to_list(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list")
    print("shopping list is ", len(shopping_list), "items long")


def show_list():
    print("Here is your shopping list:")
    for item in shopping_list:
        print(item)


def show_help():
    print("What should we pick up at the store?")
    print(""" 
    Enter 'DONE' to stop adding items
    Enter 'HELP' for this help   
    Enter 'SHOW' for view shopping list 
    """)

show_help()
while True:
    new_item = input(": ")
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()
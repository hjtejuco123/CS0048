def add_list():
    global todo_list
    task = input("Enter the task: " )
    todo_list.append(task)
    print(f"Task added successfully")
todo_list =[]

def remove_list():
    global todo_list
    print("Here are the list of todo: ", todo_list)
    numTask = input("Enter the task to remove:" )

    for i in todo_list:
        if numTask == i:
            todo_list.remove(i)
            print(f"Task removed successfully")
        else:
            print("The task is not in the list")
            break

def view_list():
    print(todo_list)
todo_list =[]
while True:
    print("======================")
    print(f"a. Add Task")
    print(f"b. Remove Task")
    print(f"c. View Task")
    
    print(f"d. Exit")
   
    choice = input("Enter your choice:")
    if choice == "a":
        add_list()
    elif choice == "b":
       remove_list()
    elif choice == "c":
       view_list()
    elif choice == "d":
        print(f"Thank you for using my program!")
        break
    else:
        print(f"Invalid choice")


    



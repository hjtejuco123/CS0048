

#using list 
#task manager  (Management System)

def task_management_system():
    #list 
    tasks = [] #list 
    
    
    def add_task():
        task = input ("Enter the task: ")
        tasks.append(task)
        print (f"Task {task} added ")
        
    def view_task():
        if tasks:
            print ("List of Task")
            for i, task in enumerate (tasks, start=1):
                print (f"{i}. {task}")
        else:
            print ("No task available")
            
    def mark_completed():
        view_task()
        try:
            task_number = int(input("Enter task to complete "))
            if 1 <= task_number <= len(tasks):
                completed_task = tasks.pop(task_number - 1)
                print (f"Task {completed_task} marked as completed ")
            else:
                print ("Invalid task number ")
        except ValueError:
            print ("Please enter a valid number! ")
        
    def delete_task():
        view_task()
        
        try:
            task_number = int(input("Enter task to delete "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print (f"task {deleted_task} delete successfully")
            else:
                print ("Invalid Task")
        except ValueError:
            print ("Please enter a valid number! ")
 
    while True:
        print ("\nTask Management System")
        print ("1. Add Task")
        print ("2. View Task")
        print ("3. Mark Task as complete")
        print ("4. Delete Task")
        print ("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print ("Exit System")
            break
        else:
            print ("Invalid choice")

    
task_management_system()


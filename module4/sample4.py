

#using list 
#task manager  (Management System)

def task_management_system():
    #list 
    tasks = [] #list 
    completed_tasks = [] #store completed task 
    
    
    def add_task():
        task = input ("Enter the task: ")
        tasks.append(task)
        print (f"Task {task} added ")
        
    def view_task():
        if tasks:
            print ("View Pending Tasks ")
            for i, task in enumerate (tasks, start=1):
                print (f"{i}. {task}")
        else:
            print ("No pending task available")
            
    def mark_completed():
        view_task()
        try:
            task_number = int(input("Enter task number to complete "))
            if 1 <= task_number <= len(tasks):
                completed_task = tasks.pop(task_number - 1)
                completed_tasks.append(completed_task)
                print (f"Task {completed_task} marked as completed ")
            else:
                print ("Invalid task number ")
        except ValueError:
            print ("Please enter a valid number! ")
        
    def view_completed_task():
        if completed_tasks:
            print ("Your completed tasked ")
            for i, task in enumerate (completed_tasks, start=1):
                print (f"{i}. {task}")
        else:
            print ("No completed task available")
    
    while True:
        print ("\nTask Management System")
        print ("1. Add Task")
        print ("2. View Pending Task")
        print ("3. Mark Task as completed")
        print ("4. View Completed Task")
        print ("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            view_completed_task()
        elif choice == "5":
            print ("Exit System")
            break
        else:
            print ("Invalid choice")

    
task_management_system()


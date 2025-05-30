def add_score():
    global subjects
    global scores
   
    subject = input("Enter subject name: ")
    score = int(input("Enter subject score: "))
    subjects.append(subject)
    scores.append(score)
    print(subjects)
    print(score)
    print("Score added!")
def  calculate_average():
    global todo_list
    task = input("Enter the task: " )
    todo_list.append(task)
    print(f"Task added successfully")


subjects = []
scores = []
def calculate_average():
    global scores
    values = scores.values()
    
    total = sum(values)

    for i in range ()
    
    print(subjects)


while True:
    print("======================")
    print(f"a. Add Score")
    print(f"b. Calculate Average")
    print(f"c. Exit")
   
    choice = input("Enter your choice:")
    if choice == "a":
        add_score()
    elif choice == "b":
       calculate_average()
    elif choice == "c":
        print(f"Thank you for using my program!")
        break
    else:
        print(f"Invalid choice")


    



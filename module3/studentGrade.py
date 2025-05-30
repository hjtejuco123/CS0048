def add_score():
 
   
    subject = input("Enter subject name: ")
    score = int(input("Enter subject score: "))
    subjects.append(subject)
    scores.append(score)
    print("Score added!")



def calculate_average():
    if not scores:
        print("Scores are empty")
    
    total = sum(scores)

    average = total /len(scores)    

    for i in range(len(subjects)):
        print(f"{subjects[i]}: {scores[i]}")
    
    print(f"Your average grade is: {average:.2f}")

subjects = []
scores = []
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


    



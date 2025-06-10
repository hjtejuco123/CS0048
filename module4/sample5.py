//Sample 5

def student_grade_management():
    
    student_records = []

    def is_unique_student_id(student_id):
        for record in student_records:
            if record[0] == student_id:  
                return False
        return True

    def add_student():
        student_id = input("Enter student ID: ")
        if not is_unique_student_id(student_id):
            print("Error: Student ID already exists. Please enter a unique ID.")
            return

        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        #Create a tuple for the student record
        student_record = (student_id, name, grade)
        student_records.append(student_record)
        print(f"Student {name} added successfully!")

    def view_students():
        if student_records:
            print("Student Records:")
            for record in student_records:
                student_id, name, grade = record  # Unpacking the tuple
                print(f"ID: {student_id}, Name: {name}, Grade: {grade}")
        else:
            print("No student records available!")

    def find_student_by_id():
        search_id = input("Enter student ID to search: ")
        found = False
        for record in student_records:
            student_id, name, grade = record
            if student_id == search_id:
                print(f"Student Found - ID: {student_id}, Name: {name}, Grade: {grade}")
                found = True
                break
        if not found:
            print("Student not found!")

    def calculate_average_grade():
        if student_records:
            total_grades = sum(grade for _, _, grade in student_records)  # Extract grades using tuple unpacking
            average_grade = total_grades / len(student_records)
            print(f"Average Grade: {average_grade:.2f}")
        else:
            print("No student records available to calculate average!")

    while True:
        print("\n--- Student Grade Management Menu ---")
        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Find Student by ID")
        print("4. Calculate Average Grade")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            calculate_average_grade()
        elif choice == "5":
            print("Exiting System!")
            break
        else:
            print("Invalid choice")

student_grade_management()

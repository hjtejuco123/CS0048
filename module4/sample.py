#student 
#student -> name, age, grade level
#student -> study, can take exam 

class Student:
    #constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
    #method    
    def study(self):
        return f"{self.name} is studing for {self.grade} grade."
    
    #method
    def take_exam(self):
        return f"{self.name} is taking an exam. "
    

#usage 

student1 = Student("Hadji", 12, "6th")
student2 = Student("Joan", 13, "8th")

print (student1.study())    #output the study method 
print (student1.take_exam()) #output the take exam method 
print (student2.study())    #output the study method 
print (student2.take_exam()) #output the take exam method 

#############################################################


#student 
#student -> name, age, grade level
#student -> study, can take exam 

class Student:
    #constructor
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 

#input 

name = input("Enter student's name: ")
grade = int(input("Enter student's grade: "))
student1 = Student(name,grade)
print (f"{student1.name} scored {student1.grade}% in the certification")


####################################################################

#student 
#student -> name, age, grade level
#student -> study, can take exam 

class Student:
    #constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
    #method    
    def study(self):
        return f"{self.name} is studing for {self.grade} grade."
    
    #method
    def take_exam(self):
        return f"{self.name} is taking an exam. "
 
class HonorsStudent(Student):
    #constructor
    def __init__(self, name, age, grade, scholarship_amout):
        super().__init__(name, age, grade)
        self.scholarship_amout = scholarship_amout
    
    #Override    
    def study(self):
        return f"{self.name} is studing intensely for {self.grade} grade honor classes."
    
    #method
    def recieve_scholarship(self):
        return f"{self.name} recieve a ${self.scholarship_amout} scholarship. "
 
 
#usage 

regular_studennt = Student("Hadji", 12, "6th")
honors_student = HonorsStudent("Joan", 13, "8th",1000)

print (regular_studennt.study())
print (honors_student.study()) 
print (honors_student.take_exam())    
print (honors_student.recieve_scholarship()) 

####################################################################

#student Management system 

class Student:
    #constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
    #method    
    def study(self):
        return f"{self.name} is studing for {self.grade} grade."
    
    #method
    def take_exam(self):
        return f"{self.name} is taking an exam. "
        
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade Level: {self.grade}. "
 
class HonorsStudent(Student):
    #constructor
    def __init__(self, name, age, grade, scholarship_amout):
        super().__init__(name, age, grade)
        self.scholarship_amout = scholarship_amout
    
    #Override    
    def study(self):
        return f"{self.name} is studing intensely for {self.grade} grade honor classes."
    
    #method
    def recieve_scholarship(self):
        return f"{self.name} recieve a ${self.scholarship_amout} scholarship. "
 
    def display_info(self):
        return f"{super().display_info()}, Scholarship amount {self.scholarship_amout}. "
 

#input part 
def get_student_info():
    print ("\nEnter student information")
    name = input("Enter name: ")
    age = input ("Enter Age: ")
    grade = input ("Enter Grade Level: ")
    return name, age, grade 


def main():
    students = []
    while True:
        print ("\nStudent Management System ")
        print ("1. Add Regular student ")
        print ("2. Add Honors student ")
        print ("3. View all students ")
        print ("4. Exit")

        choice = input ("Enter your choice 1-4: ")
        
        if choice == "1":
            name, age, grade = get_student_info()
            students.append(Student(name,age,grade))
            print ("\nRegular student added successfully")
        
        elif choice == "2":
            name, age, grade = get_student_info()
            scholarship = input ("Enter Scholarship amount: $")
            students.append(HonorsStudent(name,age,grade,scholarship))
            print ("\nHonors student added successfully")
            
        elif choice == "3":
            if not students:
                print ("\nNo student in the system yet.")
            else:
                print ("\nList of students")
                for i, student in enumerate(students, 1):
                    print (f"\nStudent #{i}: ")
                    print (student.display_info())
                    print (student.study())
                    if isinstance(student, HonorsStudent):
                        print(student.recieve_scholarship())
                    print(student.take_exam())
        
        elif choice == "4":
            print ("exit program")
            break 
    
        else:
            print ("Invalid choice")

if __name__ == "__main__":
    main()
            
####################################################################
#encapsulation

class BankAccount:
    #constructor
    def __init__ (self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.__balance = initial_balance
    
    #deposit method 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
            return f"Deposited {amount}. New balance is {self.__balance}. "
        return "Deposit amount must be positive "
    
    #withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
            return f"Withdrew {amount}. New balance is {self.__balance}. "
        return "Invalid withdrawal amount"

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.account_holder
    

account = BankAccount ("Hadji",1000)
print (account.deposit(500))
print (account.withdraw(200))
print (account.get_balance())
print (account.account_holder)


####################################################################



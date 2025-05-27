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





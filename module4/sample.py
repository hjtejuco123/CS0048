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





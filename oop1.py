class Student:
    _college = "TBC"

    def _init_(self,marks1,marks2,marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1+ self.marks2 + self.marks3)/3

    def get_marks(self):
        return self.marks1 ,self.marks2 , self.marks3

    def set_marks1(self,value):
        try:
            self.marks1 = float(value)
            
        except:
            print("unknown value, could not seen")
            
Student_A = Student(90)
print(student_A.marks1)

 

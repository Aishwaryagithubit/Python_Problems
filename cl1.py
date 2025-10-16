class Student:
    def __init__(self,name,roll_no):
     self.name = name
     self.roll_no = roll_no
     self.notebook = self.Laptop()

    def show (self):
     print(self.name,self.roll_no)

    class Laptop:

      def __init__(self):
         self.brand="Dell"
         self.cpu="core i7"
         self.ram="8 GB"

      def show(self):
         print(self.brand,self.cpu,self.ram)


s1 = Student('Andy',1)
s2 = Student('Ana',2)

s1.notebook.brand

test= Student("ABC",3).Laptop()
test.show()

print(s1.name)
print(s1.roll_no)
print(s1.notebook.show())

s1.show()
s1.notebook.show()

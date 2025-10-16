class InputOutString:
    
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

def test_class():
    obj = InputOutString()

    obj.getString()

    obj.printString()


test_class()

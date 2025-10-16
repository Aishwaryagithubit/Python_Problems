def calculate(a,b):
    sum_result=a+b
    sub_result=a-b
    return sum_result,sub_result
def takeinput():
    input1=int(input("enter first number:"))
    input2=int(input("enter second number:"))
    return input1,input2
a,b=takeinput()
sumvalue,subvalue=calculate(a,b)
print("sum:",sumvalue)
print("sub:",subvalue)
    

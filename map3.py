def num(a,b):
    return a*b

lst=[1,2,3,4,5,6,7,8,9,10]
inputNumber=int(input("enter a number"))
result=list(map(lambda a:a*inputNumber,lst))
print(list(filter(lambda a:a>10,result)))

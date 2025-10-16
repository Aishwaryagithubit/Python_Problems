'''n = int(input("Enter any number: "))
for i in (1,n+1):
   print(n*i)'''
   
'''def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)
num=int(input("Enter any number"))
result=factorial(num)
print(result) '''


# Taking input from the user
#num = int(input("Enter a number to compute its factorial: "))

# Initializing factorial to 1
#factorial = 1

# Computing factorial using a loop
'''for i in range(1, num + 1):
    factorial *= i

# Displaying the result
print(f"The factorial of {num} is: {factorial}")'''

n = int ( input ("Please enter any integer: "))
factorial = 1
for i in range (1,n+1):
  factorial = factorial * i

print ( str (n)+"! =",factorial)

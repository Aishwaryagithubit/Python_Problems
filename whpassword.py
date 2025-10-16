#force user to re-enter the name and password until name equals to saurav and password
#equals 12345 is entered

name = "saurav"
password = "12345"
n= input("enter any name:")
p=input("enter password:")
while n!=name or p!=password:
       print("Invalid try again!!")
       n=input("enter any name:")
       p=input("enter any password:")

print("welcome",n)       
    

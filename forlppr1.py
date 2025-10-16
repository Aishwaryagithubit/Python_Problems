#for i in range(0,5):
#print(i)

#len() with range
'''s= input("enter any name")
for i  in range(len(s)):
        print(s[i])
print("done") '''              

#spilt()                
s= input("enter any name")
for i  in s.split():
        print(i)
print("done") 

'''#in operator to check if an item in seq.
game = input(" what is your fav game ?")
schoolsports=['cricket','chess','tennis','baseball']
if game in schoolsports:
    print("do u like to play!!")
else:
    print("choose from given options")


#lst = [1,4,9,16,25,36,49,64,81,100]
lst =(1,4,9,16,25,36,49,64,81,100,36,36)
x=36
i=0
for num in lst:
    if (num==x):
        print ('x is 36',i)
    i+=1 

#range and for loop
#for i in range(1,101):
for i in range(100,0,-1):
  print(i)
#multiplication table
num=int(input("enter any number"))
for i in range(1,11):
    fact=num*i
    print(fact)'''
    
    

           
            

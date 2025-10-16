name=str(input("Enter any string:"))
my_numbers=[7,2,4,11,19,24,66,1,42,22,37,5,3,92,73]
if name== "even" or name=="Even" or name=="EVEN":
    even_num =[num for num in  my_numbers if num % 2 == 0]
    print("Even numbers",num)
elif name=="odd" or name=="ODD" or name=="Odd":
    odd_num = [num for num in my_numbers  if num % 2!=0]
    print("odd numbers:",odd_num)
else:
    print("unknown Input!")

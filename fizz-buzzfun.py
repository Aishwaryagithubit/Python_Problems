def num(input):
    if input%3==0:
        print("fizz")
    elif input%5==0:
        print("buzz")
    elif (input%3==0 and input%5==0):
        print("fizz_buzz")
    else:
        print("over !!")

result=num(17)


        


while True:
    try:
        n=int(input("enter any integer:"))

    except:
        print("unrecognized number!please try again!")

    else:
         print("you entered{n},your number squared is:",{n**2})
         break

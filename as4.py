string1 = str(input("Enter any string"))
string2 = str(input("Enter any string"))

len1 = len(string1)
len2 = len(string2)

if len1>len2:
    print(string1,"is longest string")
elif len2>len1:
    print(string2,"is longest string")
else:
    print("Both are longest strings")

def inc(a):
    return a+1

num=[10,20,30,40]
print(list(map(inc,num)))

print(list(map(lambda a:a+1,num)))

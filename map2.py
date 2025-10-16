def high_marks(x):
   if x>50:
        return True

lst=[10,50,60,70,80]
result=list(filter(high_marks,lst))
print(result)

result=list(filter(lambda x:x>60,lst))
print(result)

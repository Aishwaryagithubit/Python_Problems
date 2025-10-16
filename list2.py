'''nums=[10,20,30,40,50,60]
k=0
item_found=False
while k<len(nums) and not item_found:
    if nums[k] ==40:
        item_found=True
    else:
        k=k+1
if item_found:
    print("ddddd")
else:
    print("ccc") '''

ages=[10,20,30,40,50,60]
k=0
age_found=False
while k<len(ages) and not age_found:
    if ages[k]>18:
        age_found=True
        k+=1
    else:
        del ages[k]
        
if age_found:
    print(ages)
        
 


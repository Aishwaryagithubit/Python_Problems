nums=[10,20,30,40,50,60]
k=0
item_found = False
while k<len(nums) and not item_found:
    if nums[k]==40:
        item_found = True
    else:
       k=k+1

if item_found:
    print("item was found in list",k)

else:
    print("item was not found in list")

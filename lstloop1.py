nums = [10,20,30,40,50,60]

'''use for loop to iterate once for each element in a specified sequence of elements
In for loop, loop vriable i iterates automatically over sequence of values'''

#for i in nums:             
  #print(i)

#while loop (k must be initialize to 0 and incremented by 1 each time through loop
'''i=0
while i<len(nums):
    print(nums[i])
    i+=1'''

#iterating over elements
'''sum=0
for i in nums:
  sum=sum+i             
  print(sum)'''

#iterating over index value
sum=0
for i in range(len(nums)):
     sum= sum + nums[i]

print(sum)

#find average marks of students on first term exam 
marks = [[90,80],[88,93],[94,92]]
k=0
sum=0
while k in range(len(marks)):
    sum = sum + marks[k][0]
    k+=1
    
avg_marks = sum/len(marks)
print("first term marks",avg_marks)  
    
#find average marks for each students
'''k=0
sum=0
exam_avg=[]

while k<len(marks):
    sum = marks[k][0] + marks[k][1]
    avg= sum/len(marks[k])
    exam_avg.append(avg)
    k+=1
print("each student avg marks",avg)'''    

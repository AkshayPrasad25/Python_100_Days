add=[]
sum=0
student_height=input("Enter the student heights:").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
for height in student_height:
    sum+=height
no_of_students=0
for j in student_height:
    no_of_students=no_of_students+1
average=sum/no_of_students
print(f"The average height of students in College is: {average}")

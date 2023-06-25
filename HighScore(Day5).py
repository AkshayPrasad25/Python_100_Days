#inbuilt function max() & min()
student_scores=input("Enter the list of student scores: ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
max=-1
for i in student_scores:
    if(i>max):
        max=i
print(f"The Highest Score in class is {max}")
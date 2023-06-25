#range(a,b,c) function where c is step size
total=0
for i in range(2,101,2): #loops from 2->100 with step size 2(Even numbers)
    #print(i) #prints even numbers from 2->100
    total+=i
print(f"Sum of even numbers from 2->100 is {total}")

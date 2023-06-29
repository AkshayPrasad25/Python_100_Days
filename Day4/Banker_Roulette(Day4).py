import random
name=input("Enter everybody's name, separated by a comma. ")
names=name.split(", ")
no_of_people=len(names)
choice=random.randint(0,no_of_people-1)
treat=names[choice]
print(f"{treat} is going to buy meals for everyone today!")
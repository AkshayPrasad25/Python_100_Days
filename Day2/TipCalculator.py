print("Welcome to the tip calculator")
bill=float(input("What was the total bill at the restaurant?"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people=int(input("How many people to split the bill?"))
tip=tip_percentage/100*bill + bill
bill_people=tip/people
final=round(bill_people,2)
print(f"Each person should pay: {final} dollars!")
#learnt recursive functions in python 

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={"+":add, 
"-":sub,
"*":mul,
"/":div
}
def calculator():
    from Calculatorart import logo
    print(logo)
    num1=float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    not_end=True
    while not_end:
        operation_symbol=input("Pick an operation ")
        num2=float(input("Enter the next number: "))
        calculate_func= operations[operation_symbol]
        answer= calculate_func(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' if you wish to calculate with {answer}, or type 'n' to start a new calculation!! ") == 'y':
            num1=answer
        else:
            not_end=False
            calculator() #Recursion helps start new calculations

calculator()

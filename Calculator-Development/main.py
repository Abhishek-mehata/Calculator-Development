import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operation_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    # "%":mode
}
# over=False
def calculator_program():
    number1=int(input("Enter a number:"))
    for symbol in operation_dictionary:
        print(symbol)
    over=False
    while not over:
        op_symbol=str(input("Choose an operation:"))
        number2=int(input("Enter another number:"))
        calculator_function=operation_dictionary[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        decision=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit=").lower()
        if decision=='y':
            number1=output
        elif decision=='n':
            over=True
            os.system("CLS")
            calculator_program()

        elif decision=='x':
            over=True
            print("Bye..")
        else:
            pass
calculator_program()
        
   
    




#Calculator 

number1=int(input("enter first number: "))
operation=input("enter operation: ") 
number2=int(input("enter second number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "balance":
    print(number1 % number2)
else:
    print(f"{operation} is not a valid operator")

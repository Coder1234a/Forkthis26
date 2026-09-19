# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("===== Simple Calculator =====")
    print("Operations: add | subtract | multiply | divide")
    print("Type 'quit' to exit")
    print()

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.\n")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if operation == "add":
            print(f"Result: {a} + {b} = {add(a, b)}\n")
        elif operation == "subtract":
            print(f"Result: {a} - {b} = {subtract(a, b)}\n")
        elif operation == "multiply":
            print(f"Result: {a} x {b} = {multiply(a, b)}\n")
        elif operation == "divide":
            print(f"Result: {a} / {b} = {divide(a, b)}\n")

calculator()
def calculator():
    print("===== Enhanced Simple Calculator =====")
    print("Operations: add | subtract | multiply | divide | power | modulo")
    print("            sqrt | percent | factorial | average | sum")
    print("Memory:     m+ | m- | mr | mc")
    print("Other:      history | clear | quit")
    print("=" * 38 + "\n")

    memory = 0.0
    history = []

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        # Memory Operations
        if operation == "mr":
            print("Memory Recall: " + str(memory) + "\n")
            continue
        elif operation == "mc":
            memory = 0.0
            print("Memory Cleared.\n")
            continue
        elif operation == "m+":
            try:
                val = float(input("Enter number to add to memory: "))
                memory += val
                print("Memory updated: " + str(memory) + "\n")
            except ValueError:
                print("Invalid number.\n")
            continue
        elif operation == "m-":
            try:
                val = float(input("Enter number to subtract from memory: "))
                memory -= val
                print("Memory updated: " + str(memory) + "\n")
            except ValueError:
                print("Invalid number.\n")
            continue

        # Utility Operations
        if operation == "history":
            if not history:
                print("No calculations recorded yet.\n")
            else:
                print("--- Calculation History ---")
                for entry in history:
                    print(entry)
                print()
            continue

        if operation == "clear":
            history.clear()
            print("History cleared.\n")
            continue

        valid_ops = [
            "add", "subtract", "multiply", "divide", "power", 
            "modulo", "sqrt", "percent", "factorial", "average", "sum"
        ]

        if operation not in valid_ops:
            print("Invalid operation. Try again.\n")
            continue

        # Multi-number Operations (List Input)
        if operation in ["average", "sum"]:
            raw_input = input("Enter numbers separated by spaces: ")
            try:
                numbers = [float(n) for n in raw_input.split()]
                if not numbers:
                    print("No numbers provided.\n")
                    continue
            except ValueError:
                print("Please enter valid numbers only.\n")
                continue

            if operation == "sum":
                result = sum(numbers)
                entry = "Sum of " + str(numbers) + " = " + str(result)
            elif operation == "average":
                result = sum(numbers) / len(numbers)
                entry = "Average of " + str(numbers) + " = " + str(result)

            print("Result: " + entry + "\n")
            history.append(entry)
            continue

        # Single-operand Operations
        if operation in ["sqrt", "factorial"]:
            try:
                a = float(input("Enter number: "))
            except ValueError:
                print("Please enter a valid number.\n")
                continue

            if operation == "sqrt":
                if a < 0:
                    print("Error: Cannot calculate square root of a negative number.\n")
                    continue
                result = a ** 0.5
                entry = "√" + str(a) + " = " + str(result)
            elif operation == "factorial":
                if a < 0 or not a.is_integer():
                    print("Error: Factorial requires a non-negative integer.\n")
                    continue
                n = int(a)
                fact = 1
                for i in range(1, n + 1):
                    fact *= i
                result = fact
                entry = str(n) + "! = " + str(result)

            print("Result: " + entry + "\n")
            history.append(entry)
            continue

        # Two-operand Operations
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if operation == "add":
            result = a + b
            entry = str(a) + " + " + str(b) + " = " + str(result)
        elif operation == "subtract":
            result = a - b
            entry = str(a) + " - " + str(b) + " = " + str(result)
        elif operation == "multiply":
            result = a * b
            entry = str(a) + " x " + str(b) + " = " + str(result)
        elif operation == "divide":
            if b == 0:
                print("Error: Cannot divide by zero.\n")
                continue
            result = a / b
            entry = str(a) + " / " + str(b) + " = " + str(result)
        elif operation == "power":
            result = a ** b
            entry = str(a) + " ^ " + str(b) + " = " + str(result)
        elif operation == "modulo":
            if b == 0:
                print("Error: Cannot calculate modulo by zero.\n")
                continue
            result = a % b
            entry = str(a) + " % " + str(b) + " = " + str(result)
        elif operation == "percent":
            result = (a / 100) * b
            entry = str(a) + "% of " + str(b) + " = " + str(result)

        print("Result: " + entry + "\n")
        history.append(entry)

calculator()

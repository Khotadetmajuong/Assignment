while True:
    try:
        # Ask user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

    except ValueError:
        # Handles non-numeric input
        print("Invalid input! Please enter numeric values.\n")
        continue

    except ZeroDivisionError:
        # Handles division by zero
        print("Cannot divide by zero! Please enter a non-zero second number.\n")
        continue

    else:
        # If no exception occurred, print result and break the loop
        print(f"\nResult: {num1} / {num2} = {result}")
        break

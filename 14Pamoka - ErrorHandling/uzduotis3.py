def perform_operations():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        addition_result = num1 + num2
        subtraction_result = num1 - num2
        division_result = num1 / num2
        multiplication_result = num1 * num2

    except ValueError as ve:
        print(f"Error: {ve}. Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    else:
        print(f"Sum: {addition_result}")
        print(f"Subtraction: {subtraction_result}")
        print(f"Division: {division_result}")
        print(f"Multiplication: {multiplication_result}")

    finally:
        print("Thank you for using the calculator!")

perform_operations()

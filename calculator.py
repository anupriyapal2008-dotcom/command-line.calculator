def calculator():
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    selection = input("Enter the operation you want to perform (+, -, *, /): ")
    try:
        First_number = float(first_number)
        Second_number = float(second_number)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    if selection == "+":
        result= First_number + Second_number
        print("The result is: ", result)
    elif selection == "-":
        result= First_number - Second_number
        print("The result is: ", result)
    elif selection == "*":
        result= First_number * Second_number
        print("The result is: ", result)
    elif selection == "/":
        if Second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result= First_number / Second_number
            print("The result is: ", result)
    else:
        print("Invalid operation selected.")

while True:
    calculator()
    continue_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if continue_calculation.lower() != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break

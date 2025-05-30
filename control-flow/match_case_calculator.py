# Match Case Calculator

# Pront the user to input two numbers (one at a time)

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))


# Prompt the user to choose an operation
operation = input("Choose the operation (+, -, *, /): ")


# implement Match Case statement
match operation:
    case "+":
	result = num1 + num2
	print(f"The result is {result}.")

    case "-":
	result = num1 - num2
	print(f"The result is {result}.")

    case "*":
	result = num1 * num2
	print(f"The result is {result}.")

    case "/":
	if num2 == 0:
	    print("Cannot divide by zero.")

	else:
	    result = num1 / num2
	    print(f"The result is {result}.")

    case _:
	print("Invalid operation selected.")

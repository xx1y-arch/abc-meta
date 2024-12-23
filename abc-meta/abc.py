import time

# Function to calculate factorial
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        print(result)  # Printing at every step, bad for performance
    return result

# Infinite loop to get user input and calculate factorial
while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)  # No validation for non-integer strings
        if number < 0:
            print("Factorial of negative numbers is not defined.")  # Poor feedback
            continue
        result = calculate_factorial(number)
        print(f"The factorial of {number} is: {result}")
        time.sleep(1)  # Unnecessary delay for user experience
    except ValueError as e:
        print("Please enter a valid number.")  # Catch-all error handling, poor feedback
    except Exception as e:
        print("Something went wrong.")  # Generic error message, not helpful

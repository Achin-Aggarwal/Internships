def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x // y

def display_menu():
    print("\nAdvanced Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    print("8. View Calculation History")
    print("9. Clear Calculation History")
    print("10. Exit")

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None, None

def display_history(history):
    if not history:
        print("No history available.")
    else:
        print("\nCalculation History:")
        for i, record in enumerate(history, start=1):
            print(f"{i}. {record}")

def main():
    history = []
    last_result = None

    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if last_result is not None:
                use_last_result = input("Use the last result? (yes/no): ").strip().lower()
                if use_last_result == 'yes':
                    num1 = last_result
                    num2 = float(input("Enter the next number: "))
                else:
                    num1, num2 = get_user_input()
            else:
                num1, num2 = get_user_input()

            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2}"
            elif choice == '5':
                result = modulus(num1, num2)
                operation = f"{num1} % {num2}"
            elif choice == '6':
                result = exponentiate(num1, num2)
                operation = f"{num1} ** {num2}"
            elif choice == '7':
                result = floor_divide(num1, num2)
                operation = f"{num1} // {num2}"

            print(f"Result: {result}")
            history.append(f"{operation} = {result}")
            last_result = result

        elif choice == '8':
            display_history(history)
        
        elif choice == '9':
            history.clear()
            print("Calculation history cleared.")
        
        elif choice == '10':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()

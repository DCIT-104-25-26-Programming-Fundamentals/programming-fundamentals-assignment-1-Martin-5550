# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# =============================================================================

def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """
    Returns the result of a / b, rounded to 2 decimal places.
    Returns None if b is zero (division by zero).
    """
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of a % b.
    Returns None if b is zero (division by zero).
    """
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Prints the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_two_numbers():
    """Prompts for and returns two numbers as a tuple."""
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second


def format_number(value):
    """Formats a number without a trailing '.0' for whole-number floats."""
    if value == int(value):
        return str(int(value))
    return str(value)


def main():
    while True:
        print()
        display_menu()
        choice = input("Select an operation (1-7): ")
        print()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            continue

        first, second = get_two_numbers()

        if choice == "1":
            result = add(first, second)
            print(
                f"Result: {format_number(first)} + {format_number(second)} = {format_number(result)}")

        elif choice == "2":
            result = subtract(first, second)
            print(
                f"Result: {format_number(first)} - {format_number(second)} = {format_number(result)}")

        elif choice == "3":
            result = multiply(first, second)
            print(
                f"Result: {format_number(first)} * {format_number(second)} = {format_number(result)}")

        elif choice == "4":
            result = divide(first, second)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(
                    f"Result: {format_number(first)} / {format_number(second)} = {result}")

        elif choice == "5":
            result = modulus(first, second)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(
                    f"Result: {format_number(first)} % {format_number(second)} = {format_number(result)}")

        elif choice == "6":
            result = exponentiate(first, second)
            print(
                f"Result: {format_number(first)} ** {format_number(second)} = {format_number(result)}")


if __name__ == "__main__":
    main()

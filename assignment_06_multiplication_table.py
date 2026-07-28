# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# =============================================================================

def print_table(number):
    """
    Prints the multiplication table for 'number' from 1 to 12.
    """
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number}  x  {i:<2} =  {result}")


def print_tables_up_to_n(n):
    """
    Prints multiplication tables for every number from 1 to n,
    separated by a line of dashes.
    """
    for number in range(1, n + 1):
        print_table(number)
        print("-" * 29)


def do_single_table():
    """Handles Part A: asks for a number and prints its table."""
    number = int(input("Enter a number: "))
    print()
    print_table(number)


def do_tables_range():
    """Handles Part B: asks for N and prints tables from 1 to N."""
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to_n(n)


def main():
    print("Multiplication Table Generator")
    print("1. Single Table (Part A)")
    print("2. Tables from 1 to N (Part B - Bonus)")

    choice = input("Choose an option (1-2): ")

    if choice == "1":
        do_single_table()
    elif choice == "2":
        do_tables_range()
    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()

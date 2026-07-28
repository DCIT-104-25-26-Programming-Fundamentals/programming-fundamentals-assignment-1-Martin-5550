# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# =============================================================================

def generate_fibonacci_terms(n):
    """
    Returns a list containing the first n terms of the Fibonacci sequence,
    generated using a loop (not recursion).
    """
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci_number(number):
    """
    Determines whether 'number' appears in the Fibonacci sequence,
    using a loop (not recursion).
    """
    if number < 0:
        return False

    a, b = 0, 1

    # Walk the sequence until we reach or pass the target number
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False


def print_first_n_terms():
    """Handles Part A: asks for N and prints the first N Fibonacci terms."""
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: The number of terms must be a positive integer.")
        return

    terms = generate_fibonacci_terms(n)
    terms_as_strings = [str(term) for term in terms]
    print("Fibonacci sequence:", " ".join(terms_as_strings))


def check_fibonacci_membership():
    """Handles Part B: asks for a number and checks if it's a Fibonacci number."""
    number = int(input("Enter a number to check: "))

    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    print_first_n_terms()
    print()
    check_fibonacci_membership()


if __name__ == "__main__":
    main()

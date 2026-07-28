"""Prime Number Checker.

Checks whether a user-entered number is a prime number.
"""


def is_prime(number):
    """Return True if number is a prime number, False otherwise."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    """Prompt the user for a number and report whether it is prime."""
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")


if __name__ == "__main__":
    main()

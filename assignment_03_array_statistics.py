# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# =============================================================================

def calculate_sum(numbers):
    """Returns the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Returns the average of the numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    """Returns the largest number in the list (no built-in max())."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_min(numbers):
    """Returns the smallest number in the list (no built-in min())."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def get_numbers(count):
    """Prompts the user for 'count' numbers and returns them as a list."""
    numbers = []
    for i in range(1, count + 1):
        value = int(input(f"Enter number {i}: "))
        numbers.append(value)
    return numbers


def main():
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: The number of values must be a positive integer.")
        return

    numbers = get_numbers(count)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    highest = calculate_max(numbers)
    lowest = calculate_min(numbers)

    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {highest}")
    print(f"Minimum: {lowest}")


if __name__ == "__main__":
    main()

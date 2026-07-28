# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# =============================================================================

def read_matrix(name="Matrix"):
    """
    Reads an M x N matrix from the user, one row at a time,
    with values separated by spaces. Returns a 2D list.
    """
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    matrix = []
    for i in range(1, rows + 1):
        row_values = input(f"Enter row {i}: ").split()
        row = [int(value) for value in row_values]

        # Basic safety check: make sure the row has the expected length
        if len(row) != cols:
            print(
                f"Error: Expected {cols} values, got {len(row)}. Please re-enter the row.")
            row_values = input(f"Enter row {i}: ").split()
            row = [int(value) for value in row_values]

        matrix.append(row)

    return matrix


def print_matrix(matrix, label="Matrix"):
    """Displays a matrix in a neat, aligned grid format."""
    print(f"\n{label}:")
    for row in matrix:
        # Right-align each number in a fixed-width field for a clean grid
        formatted_row = "  ".join(f"{value:>4}" for value in row)
        print(formatted_row)


def transpose_matrix(matrix):
    """
    Returns the transpose of the given matrix
    (rows become columns, columns become rows).
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty cols x rows matrix to hold the result
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """
    Returns the element-wise sum of two matrices of the same size.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    Returns the matrix product A x B.
    A is M x N, B is N x P, result is M x P.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][i if False else j]
            result[i][j] = total

    return result


def do_transpose():
    matrix = read_matrix("the Matrix")
    print_matrix(matrix, "Original Matrix")

    transposed = transpose_matrix(matrix)
    print_matrix(transposed, "Transposed Matrix")


def do_addition():
    print("\n-- Matrix A --")
    matrix_a = read_matrix("Matrix A")
    print("\n-- Matrix B --")
    matrix_b = read_matrix("Matrix B")

    # Validate that dimensions match
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Error: Matrices must be the same size to add them.")
        return

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    result = add_matrices(matrix_a, matrix_b)
    print_matrix(result, "Sum (A + B)")


def do_multiplication():
    print("\n-- Matrix A (M x N) --")
    matrix_a = read_matrix("Matrix A")
    print("\n-- Matrix B (N x P) --")
    matrix_b = read_matrix("Matrix B")

    # Validate that A's columns match B's rows
    if len(matrix_a[0]) != len(matrix_b):
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(result, "Product (A x B)")


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an operation (1-3): ")

    if choice == "1":
        do_transpose()
    elif choice == "2":
        do_addition()
    elif choice == "3":
        do_multiplication()
    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()

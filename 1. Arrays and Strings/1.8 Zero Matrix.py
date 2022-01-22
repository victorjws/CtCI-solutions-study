# Solution 1. O(N) space. even use a bit vector instead of a boolean array
def set_zeros(matrix: list[list[int]]) -> None:
    row = [False for _ in range(len(matrix))]
    column = [False for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    # Nullify rows
    for i in range(len(matrix)):
        if row[i]:
            nullify_row(matrix, i)
    for j in range(len(matrix[0])):
        if column[j]:
            nullify_column(matrix, j)


def nullify_row(matrix: list[list[int]], row: int) -> None:
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix: list[list[int]], col: int) -> None:
    for i in range(len(matrix)):
        matrix[i][col] = 0


# Solution 2. O(1) space.
def set_zeros_2(matrix: list[list[int]]) -> None:
    row_has_zero = False
    col_has_zero = False

    # Check if first row has a zero
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
            break

    # Check if first column has a zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    # Check for zeros in the rest of the array
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify rows based on values in first column
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    # Nullify columns based on values in first row
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    # Nullify first row
    if row_has_zero:
        nullify_row(matrix, 0)

    # Nullify first column
    if col_has_zero:
        nullify_column(matrix, 0)


# My Solution
def find_zeros(
    matrix: list[list[int]],
    rows: int,
    cols: int
    # ) -> list[tuple[int, int]]:
) -> int:
    # zero_coordinates = []
    # for r in range(rows):
    #     for c in range(cols):
    #         print(f"matrix[{r}][{c}] = {matrix[r][c]}")
    #         if matrix[r][c] == 0:
    #             zero_coordinates.append((r, c))
    zero_coordinates = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_coordinates |= 1 << (r * cols + c + 1)
    return zero_coordinates


def update_zeros(
    matrix: list[list[int]],
    rows: int,
    cols: int,
    # zero_coordinates: list[tuple[int, int]],
    zero_coordinates: int,
) -> list[list[int]]:
    # for r, c in zero_coordinates:
    #     for x in range(rows):
    #         matrix[x][c] = 0
    #     for y in range(cols):
    #         matrix[r][y] = 0
    for r in range(rows):
        for c in range(cols):
            if zero_coordinates & 1 << (r * cols + c + 1):
                for x in range(rows):
                    matrix[x][c] = 0
                for y in range(cols):
                    matrix[r][y] = 0
    return matrix


def update_zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        raise Exception("There's no matrix")
    rows = len(matrix)
    cols = len(matrix[0])
    zero_coordinates = find_zeros(matrix, rows, cols)
    return update_zeros(matrix, rows, cols, zero_coordinates)


N = int(input())
MATRIX = list(list(map(int, input().split())) for _ in range(N))
# MATRIX = update_zero_matrix(MATRIX)
set_zeros_2(MATRIX)
for row in MATRIX:
    print(row)

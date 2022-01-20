# Solution O(N^2)
def rotate1(matrix: list[list[int]]) -> bool:
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # save top

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return True


# My Solution
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    rotated = []
    for x in range(n):
        # row = [matrix[y][n - x - 1] for y in range(n)]  # -90 degree rotate
        row = [matrix[n - y - 1][x] for y in range(n)]  # 90 degree rotate
        rotated.append(row)
    return rotated


from copy import deepcopy


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
# result = rotate1(deepcopy(M))
# for r in result:
#     print(r)
print("---------------")
result = rotate(deepcopy(M))
for r in result:
    print(r)

# input data
# 5
# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55


# x, y - y, n - x
# [
#     [1,2,3]
# ]
#
# 1,1 -> 1,4
# 1,2 - 2, 4
# 1,3 = 3, 4
# 1, 4 - 4, 4
#
# 2, 1 - 1, 3
# 2,2 - 2, 3
# 2,3 - 3, 3
# 4, 3 - 4, 3
#
# 3, 1 - 1, 2
# 3, 2 - 2, 2
# 3, 3 - 3, 2
# 3, 4 - 4, 2
#
# 4, 1 - 1, 1
# 4, 2 - 2, 1
# 4, 3 - 3, 1
# 4, 4 - 4, 1
#
#
#
# 1,1 - 1,5
# 1,2 - 2,5
# 1,3 - 3,5
# 1,4 - 4,5
# 1,5 - 5,5
#
# 3,1 - 1,3
# 3,2 - 2,3
# 3,3 - 3,3
# 3,4 - 4,3
# 3,5 - 5,3

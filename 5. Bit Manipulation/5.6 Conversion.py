# Solution 1.
def bit_swap_required(a: int, b: int) -> int:
    count = 0
    c = a ^ b
    while c != 0:
        count += c & 1
        c >>= 1
    return count


# Solution 2.
def bit_swap_required2(a: int, b: int) -> int:
    count = 0
    c = a ^ b
    while c != 0:
        c &= c - 1
        count += 1
    return count


# My Solution
def bit_diff(n1: int, n2: int) -> int:
    diff = n1 ^ n2
    count = 0
    while diff >= 1:
        if diff % 2 == 1:
            count += 1
        diff //= 2
    return count


print(bit_diff(29, 15))
print(bit_swap_required(29, 15))
print(bit_swap_required2(29, 15))

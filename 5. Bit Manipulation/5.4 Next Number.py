# Solution. Bit Manipulation Approach.
def get_next(n: int) -> int:
    # Compute c0 and c1
    c, c0, c1 = n, 0, 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # Error: if n == 11..1100...00, then there is no bigger number with the
    # same number of 1s.
    if c0 + c1 == 31 or c0 + c1 == 1:
        return -1

    p = c0 + c1  # position of rightmost non-trailing zero

    n |= 1 << p  # Flip rightmost non-trailing zero
    n &= ~((1 << p) - 1)  # Clear all bits to the right of p
    n |= (1 << (c1 - 1)) - 1  # Insert (c1-1) ones on the right.

    return n


def get_prev(n: int) -> int:
    temp, c0, c1 = n, 0, 0
    while temp & 1 == 1:
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1

    while ((temp & 1) == 0) and (temp != 0):
        c0 += 1
        temp >>= 1

    p = c0 + c1  # position of rightmost non-trailing one
    n &= (~0) << (p + 1)  # clears from bit p onwards

    mask = (1 << (c1 + 1)) - 1  # Sequence of (c1+1) ones
    n |= mask << (c0 - 1)

    return n


# Solution. Arithmetic Approach.
def get_next_arith(n: int) -> int:
    # ... same calculation for c0 and c1 as before ...
    c, c0, c1 = n, 0, 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    if c0 + c1 == 31 or c0 + c1 == 1:
        return -1

    return n + (1 << c0) + (1 << (c1 - 1)) - 1


def get_prev_arith(n: int) -> int:
    temp, c0, c1 = n, 0, 0
    while temp & 1 == 1:
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1

    while ((temp & 1) == 0) and (temp != 0):
        c0 += 1
        temp >>= 1

    return n - (1 << c1) - (1 << (c0 - 1)) + 1


# My Solution. Wrong Answer
class Integer:
    BYTES = 4


def print_bin_repr(n: int):
    count = get_1_count(n)
    big = get_bigger_number(count)
    p_small = get_positive_smaller_number(count)
    n_small = get_negative_smaller_number(count)
    print(f"big: {bin(big)}")
    print(f"positive_small: {bin(p_small)}")
    print(f"negative_small: {bin(n_small)}")


def get_1_count(n: int) -> int:
    count = 0
    while n >= 1:
        rest = n % 2
        if rest == 1:
            count += 1
        n //= 2
    return count


def get_bigger_number(count: int) -> int:
    zero_length = Integer.BYTES * 8 - count
    result = 0
    for i in range(count):
        result = result | 1 << (zero_length + i)
    return result


def get_positive_smaller_number(count: int) -> int:
    result = 0
    for i in range(count):
        result = result | 1 << i
    return result


def get_negative_smaller_number(count: int) -> int:
    zero_length = Integer.BYTES * 8 - count
    result = 0
    for i in range(count - 1):
        result = result | 1 << (zero_length + i)
    return -result


num = int(input())
print_bin_repr(num)
print(get_next(num))
print(get_prev(num))
print(get_next_arith(num))
print(get_prev_arith(num))

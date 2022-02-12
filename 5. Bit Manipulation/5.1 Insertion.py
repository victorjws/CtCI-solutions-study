# Solution 1.
def update_bits(n: int, m: int, i: int, j: int) -> int:
    # Create a mask to clear bits i through j in n.
    # For simplicity, we'll use just 8 bits for the example.
    all_ones = ~0  # will equal sequence of all 1s

    # 1s before position j, then 0s. left = 11100000
    left = all_ones << (j + 1)

    # 1's after position i. right = 0000011
    right = (1 << i) - 1

    # All 1s, except for 0s between i and j. mask = 11100011
    mask = left | right

    # Clear bits j through i then put m in there.
    n_cleared = n & mask  # Clear bits j through i.
    m_shifted = m << i  # Move m into correct position.
    return n_cleared | m_shifted  # OR them, and we're done!


# My Solution.
def insert_bit(n_str: str, m_str: str, i: int, j: int) -> str:
    n = int(n_str, 2)
    m = int(m_str, 2)
    mask = get_mask(i, j)
    result = n & mask
    m = m << i
    result = result | m
    return bin(result)


def get_mask(i, j) -> int:
    length = j - i + 1
    mask = "1" * length
    mask = int(mask, 2)
    mask = mask << i
    mask = ~mask
    return mask


print(update_bits(int("10000000000", 2), int("10011", 2), 2, 6))
print(int(insert_bit("10000000000", "10011", 2, 6), 2))
print(update_bits(int("11111111", 2), int("010", 2), 1, 3))
print(int(insert_bit("11111111", "010", 1, 3), 2))

# Solution 1
# O(N) time, N is the length of the string.
def is_permutation_of_palindrome1(phrase: str) -> bool:
    table = build_char_frequency_table(phrase)
    return check_max_one_odd(table)


def check_max_one_odd(table: list[int]) -> bool:
    found_odd = False
    for count in table:
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def get_char_number(c: str) -> int:
    a = ord("a")
    z = ord("z")
    val = ord(c)
    if a <= val <= z:
        return val - a
    return -1


def build_char_frequency_table(phrase: str) -> list[int]:
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
    return table


# Solution 2
# O(N) but might be slightly slower.
def is_permutation_of_palindrome2(phrase: str) -> bool:
    count_odd = 0
    table = [0 for _ in range(ord("z") - ord("a") + 1)]

    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


# Solution 3
def is_permutation_of_palindrome3(phrase: str) -> bool:
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


def create_bit_vector(phrase: str) -> int:
    bit_vector = 0
    for c in phrase:
        x = get_char_number(c)
        bit_vector = toggle(bit_vector, x)
        # bit_vector ^= 1 << x
    return bit_vector


def toggle(bit_vector: int, index: int) -> int:
    if index < 0:
        return bit_vector

    mask: int = 1 << index
    if bit_vector & mask == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector


def check_exactly_one_bit_set(bit_vector: int) -> bool:
    return bit_vector & (bit_vector - 1) == 0


p = input()
print(is_permutation_of_palindrome1(p))
print(is_permutation_of_palindrome2(p))
print(is_permutation_of_palindrome3(p))

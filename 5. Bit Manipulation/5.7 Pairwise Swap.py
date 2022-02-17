# Solution.
def swap_odd_even_bits(x: int) -> int:
    # use logical shift because we want the sign bit to be filled with a zero.
    return ((x & 0xAAAAAAAA) >> 1) | ((x & 0x55555555) << 1)


# My Solution.
def swap(n: int) -> int:
    odd_mask = int("55555555", 16)
    even_mask = int("AAAAAAAA", 16)
    odd = n & odd_mask
    even = n & even_mask
    odd <<= 1
    even >>= 1
    return odd | even


print(bin(1233))
print(bin(swap(1233)))
print(bin(swap_odd_even_bits(1233)))

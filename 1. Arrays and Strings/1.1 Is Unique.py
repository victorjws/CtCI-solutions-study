# Solution
def is_unique(string: str) -> bool:
    if len(string) > 128:  # ASCII characters. Check 256 if extended ASCII.
        return False

    checker = 0
    for s in string:
        val = ord(s) - ord("a")
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True


print(is_unique(input()))

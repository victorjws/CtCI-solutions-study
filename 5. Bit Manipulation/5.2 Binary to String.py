# Solution 1.
def print_binary(num: float) -> str:
    if num >= 1 or num <= 0:
        return "ERROR"

    binary = "."
    while num > 0:
        # Setting a limit on length: 32 characters
        if len(binary) >= 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            binary += "1"
            num = r - 1
        else:
            binary += "0"
            num = r
    return binary


# Solution 1.
def print_binary2(num: float) -> str:
    if num >= 1 or num <= 0:
        return "ERROR"

    binary = "."
    frac = 0.5

    while num > 0:
        # Setting a limit on length: 32 characters
        if len(binary) > 32:
            return "ERROR"
        if num >= frac:
            binary += "1"
            num -= frac
        else:
            binary += "0"
        frac /= 2
    return binary


# My Solution.
def bin_to_str(n: float) -> str:
    if not 0 < n < 1:
        return "ERROR"
    result = "0."
    count = 0
    while n != 0:
        count += 1
        if count > 32:
            return "ERROR"
        n *= 2
        if n >= 1:
            n -= 1
            result += "1"
        else:
            result += "0"
    return result


print(bin_to_str(0.125))
print(print_binary(0.125))
print(print_binary2(0.125))

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

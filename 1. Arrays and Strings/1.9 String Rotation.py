# Solution. if isSubstring runs in O(A+B) time (on strings  of length A and B),
# then the runtime of isRotation is O(N). N is length of string
def is_rotation(s1: str, s2: str) -> bool:
    length = len(s1)
    # Check that s1 and s2 are equal length and not empty
    if length == len(s2) and length > 0:
        # Concatenate s1 and s1 within new buffer
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    return False


# My Solution
def is_substring(string1, string2):
    if string1 in string2:
        return True
    return False


def is_rotated_string(s1: str, s2: str) -> bool:
    s2 = s2 * 2
    if is_substring(s1, s2):
        return True
    return False


print(is_rotated_string(*input().split()))

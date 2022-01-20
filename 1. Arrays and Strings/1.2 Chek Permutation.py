# Solution 1
def check_permutation1(string1: str, string2: str) -> bool:
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if len(string1) != len(string2):
        return False

    if sorted(string1) == sorted(string2):
        return True
    return False


# Solution 2
def check_permutation2(string1: str, string2: str) -> bool:
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if len(string1) != len(string2):
        return False

    letters = [0 for _ in range(128)]

    for s1 in string1:
        letters[ord(s1)] += 1

    for s2 in string2:
        letters[ord(s2)] -= 1
        if letters[ord(s2)] < 0:
            return False
    return True


print(check_permutation2(*input().split()))

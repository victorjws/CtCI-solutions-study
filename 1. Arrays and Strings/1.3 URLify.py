# Solution
from typing import List


def replace_spaces(string: List[str], true_length: int) -> str:
    space_count = 0

    for i in range(true_length):
        if string[i] == " ":
            space_count += 1

    index = true_length + space_count * 2

    if space_count > 0:
        string.extend(["" for _ in range(space_count * 2 + 1)])

    for i in range(true_length - 1, -1, -1):
        if string[i] == " ":
            string[index - 1] = "0"
            string[index - 2] = "2"
            string[index - 3] = "%"
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1

    return "".join(string)


s, length = input().split(",")
print(replace_spaces(list(s), int(length)))

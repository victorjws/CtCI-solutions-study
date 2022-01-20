# Solution
def one_edit_away(first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:
        return False

    shorter = first if len(first) < len(second) else second
    longer = second if len(first) < len(second) else first
    shorter_index = 0
    longer_index = 0
    found_difference = False
    while shorter_index < len(shorter) and longer_index < len(longer):
        if shorter[shorter_index] != longer[longer_index]:
            if found_difference:
                return False
            found_difference = True
            if len(shorter) == len(longer):
                shorter_index += 1
        else:
            shorter_index += 1
        longer_index += 1
    return True


# def one_edit_away(string1: str, string2: str) -> bool:
#     if len(string1) >= len(string2):
#         longer_list = list(string1)
#         shorter_list = list(string2)
#     else:
#         longer_list = list(string2)
#         shorter_list = list(string1)
#     if len(longer_list) - len(shorter_list) == 1:
#         index = 0
#         for c1 in longer_list:
#             if c1 == shorter_list[index]:
#                 index += 1
#             if len(shorter_list) == index:
#                 return True
#     elif len(longer_list) - len(shorter_list) == 0:
#         changed = 0
#         for i, c1 in enumerate(longer_list):
#             if c1 != shorter_list[i]:
#                 changed += 1
#                 if changed > 1:
#                     return False
#         if changed == 1:
#             return True
#     return False


print(one_edit_away(*input().split()))

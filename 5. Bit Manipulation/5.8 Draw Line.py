# Solution.
def draw_line_1(
    screen: list[int], width: int, x1: int, x2: int, y: int
) -> None:
    start_offset = x1 % 8
    first_full_byte = x1 // 8
    if start_offset != 0:
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = x2 // 8
    if end_offset != 7:
        last_full_byte -= 1

    # Set full bytes
    for b in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + b] = 0xFF

    # Create masks for start and end of line
    start_mask = 0xFF >> start_offset
    end_mask = (
        ~(0xFF >> (end_offset + 1)) & 255
    )  # '& 255' for python bitwise NOT

    # Set start and end of line
    if (x1 // 8) == (x2 // 8):  # x1 and x2 are in the same byte
        mask = start_mask & end_mask
        screen[(width // 8) * y + (x1 // 8)] |= mask
    else:
        if start_offset != 0:
            byte_number = (width // 8) * y + first_full_byte - 1
            screen[byte_number] |= start_mask
        if end_offset != 7:
            byte_number = (width // 8) * y + last_full_byte + 1
            screen[byte_number] |= end_mask


# My Solution.
def draw_line(screen: list, width: int, x1: int, x2: int, y: int) -> list:
    if width < x2:
        raise Exception("Exceed coordinates")
    if x1 > x2:
        x1, x2 = x2, x1

    line = hex((pow(2, width + 1 - x1) - 1) & (-1 << (width - x2)))
    width_len = width // 8
    line_num = width_len * y

    for i in range(width_len):
        screen[line_num + i] |= int(line[(i + 1) * 2 : (i + 1) * 2 + 2], 16)
    return screen


s = [0, 0, 0, 0, 0, 0, 0, 0]
w = 16
x1_ = 3
x2_ = 10
y_ = 1
# result = draw_line(s, w, x1_, x2_, y_)
draw_line_1(s, w, x1_, x2_, y_)
result = s
width_l = w // 8
string = ""
for i, val in enumerate(result):
    string += format(val, "010b")[2:]
    if i % width_l == width_l - 1:
        print(string)
        string = ""

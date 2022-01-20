def compress1(string: str) -> str:
    compressed = []
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    compressed_string = "".join(compressed)
    return compressed_string if len(compressed_string) < len(string) else string


def compress2(string: str) -> str:
    final_length = count_compression(string)
    if final_length >= len(string):
        return string

    compressed = []
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    compressed_string = "".join(compressed)
    return compressed_string


def count_compression(string: str) -> int:
    compressed_length = 0
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed_length += 1 + len(str(count_consecutive))
            count_consecutive = 0
    return compressed_length


data = input()
print(compress1(data))
print(compress2(data))

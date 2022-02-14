# Solution: Brute Force
# O(b) time and O(b) memory, where b is the length of the sequence.
class Integer:
    BYTES = 4


def longest_sequence(n: int) -> int:
    if n == -1:
        return Integer.BYTES * 8  # in java
    sequences = get_alternating_sequences(n)
    return find_longest_sequence(sequences)


# Return a list of the sizes of the sequences.
# The sequence starts off with the number of 0s (which might be 0) and then
# alternates with the counts of each value.
def get_alternating_sequences(n: int) -> list[int]:
    sequences = []

    searching_for = 0
    counter = 0

    for i in range(Integer.BYTES * 8):
        if (n & 1) != searching_for:
            sequences.append(counter)
            searching_for = n & 1  # Flip 1 to 0 or 0 to 1
            counter = 0
        counter += 1
        n >>= 1  # n >>>= 1  # in java
    sequences.append(counter)
    return sequences


# Given the lengths of alternating sequences of 0s and 1s, find the longest one
# we can build.
def find_longest_sequence(seq: list[int]) -> int:
    max_seq = 1

    for i in range(0, len(seq), 2):
        zeros_seq = seq[i]
        ones_seq_right = seq[i - 1] if i - 1 >= 0 else 0
        ones_seq_left = seq[i + 1] if i + 1 < len(seq) else 0

        this_seq = 0
        if zeros_seq == 1:  # Can merge
            this_seq = ones_seq_left + 1 + ones_seq_right
        elif zeros_seq > 1:  # Just add a zero to either side
            this_seq = 1 + max(ones_seq_right, ones_seq_left)
        elif zeros_seq == 0:  # No zero, but take either side
            this_seq = max(ones_seq_right, ones_seq_left)
        max_seq = max(this_seq, max_seq)
    return max_seq


# Solution: Optimal Algorithm.
# O(b) time, O(1) additional memory
def flip_bit(a: int) -> int:
    # If all 1s, this is already the longest sequence.
    if ~a == 0:
        return Integer.BYTES * 8

    current_length = 0
    previous_length = 0
    max_length = 1  # We can always have a sequence of at least one 1
    while a != 0:
        if (a & 1) == 1:  # Current bit is a 1
            current_length += 1
        elif (a & 1) == 0:  # Current bit is a 0
            # Update to 0 (if next bit is 0) or current_length (if next bit is
            # 1).
            previous_length = 0 if (a & 2) == 0 else current_length
            current_length = 0
        max_length = max(previous_length + current_length + 1, max_length)
        a >>= 1  # a >>>= 1 # in java
    return max_length


# My Solution.
def flip(num: int) -> int:
    n_str = bin(num)[2:]
    count = 0
    now = "1"
    counted = []
    for i in n_str:
        if now == i:
            count += 1
        else:
            counted.append((now, count))
            now = "0" if now == "1" else "1"
            count = 1
    counted.append((now, count))
    max_length = counted[0][1]
    i = 0
    while len(counted) - 2 > i:
        if (
            counted[i][0] == "1"
            and counted[i + 1][1] == 1
            and max_length < counted[i][1] + counted[i + 2][1]
        ):
            max_length = counted[i][1] + counted[i + 2][1] + 1
        i += 1
    return max_length


print(flip(1775))
print(longest_sequence(1775))
print(flip_bit(1775))

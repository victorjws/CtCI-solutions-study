# Solution.
# Simulates
breaking_point: int = ...
count_drops: int = 0


def drop(floor: int) -> bool:
    global count_drops, breaking_point
    count_drops += 1
    return floor >= breaking_point


def find_breaking_point(floors: int) -> int:
    global breaking_point
    interval = 14
    previous_floor = 0
    egg1 = interval
    breaking_point = floors

    # Drop egg1 at decreasing intervals.
    while (not drop(egg1)) and egg1 <= floors:
        interval -= 1
        previous_floor = egg1
        egg1 += interval

    # Drop egg2 at 1 unit increments.
    egg2 = previous_floor + 1
    while egg2 < egg1 and egg2 <= floors and (not drop(egg2)):
        egg2 += 1

    # If it didn't break, return -1.
    return -1 if egg2 > floors else egg2


find_breaking_point(10)
print(count_drops)

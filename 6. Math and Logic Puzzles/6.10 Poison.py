# Solution 1: Naive Approach (28 days).
import random


class Bottle:
    poisoned = False

    def __init__(self, id_: int):
        self.id_num = id_

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_num})"

    def get_id(self) -> int:
        return self.id_num

    def set_as_poisoned(self) -> None:
        self.poisoned = True

    def is_poisoned(self) -> bool:
        return self.poisoned


class TestStrip:
    DAYS_FOR_RESULT = 7

    def __init__(self, id_: int):
        self.id_num = id_
        self.drops_by_day: list[list[Bottle]] = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_num})"

    def get_id(self) -> int:
        return self.id_num

    # Resize list of days/drops to be large enough.
    def size_drops_for_day(self, day: int) -> None:
        while len(self.drops_by_day) <= day:
            bottles: list[Bottle] = []
            self.drops_by_day.append(bottles)

    # Add drop from bottle on specific day.
    def add_drop_on_day(self, day: int, bottle: Bottle) -> None:
        self.size_drops_for_day(day)
        drops: list[Bottle] = self.drops_by_day[day]
        drops.append(bottle)

    # Checks if any of the bottles in the set are poisoned.
    def has_poison(self, bottles: list[Bottle]) -> bool:
        for b in bottles:
            if b.is_poisoned():
                return True
        return False

    # Gets bottles used in the test DAYS_FOR_RESULT days ago.
    def get_last_weeks_bottles(self, day: int) -> list[Bottle]:
        if day < self.DAYS_FOR_RESULT:
            return None
        return self.drops_by_day[day - self.DAYS_FOR_RESULT]

    # Checks for poisoned bottles since before DAYS_FOR_RESULT
    def is_positive_on_day(self, day: int) -> bool:
        test_day = day - self.DAYS_FOR_RESULT
        if test_day < 0 or test_day >= len(self.drops_by_day):
            return False
        for d in range(test_day + 1):
            bottles: list[Bottle] = self.drops_by_day[d]
            if self.has_poison(bottles):
                return True
        return False


# Distribute bottles across test strips evenly.
def run_test_set(
    bottles: list[Bottle], strips: list[TestStrip], day: int
) -> None:
    index = 0
    for bottle in bottles:
        strip = strips[index]
        strip.add_drop_on_day(day, bottle)
        index = (index + 1) % len(strips)


def find_poisoned_bottle(bottles: list[Bottle], strips: list[TestStrip]) -> int:
    today = 0

    while len(bottles) > 1 and len(strips) > 0:
        # Run tests.
        run_test_set(bottles, strips, today)

        # Wait for results.
        today += TestStrip.DAYS_FOR_RESULT

        # Check results.
        for strip in strips:
            if strip.is_positive_on_day(today):
                bottles = strip.get_last_weeks_bottles(today)
                strips.remove(strip)
                break

    if len(bottles) == 1:
        print(f"total_day:{today}")
        return bottles[0].get_id()
    return -1


b = [Bottle(i + 1) for i in range(1000)]
b[random.randint(0, 1000)].set_as_poisoned()
s = [TestStrip(i) for i in range(10)]
print(find_poisoned_bottle(b, s))


# Solution 2: Optimized Approach (10 days).
# |         | Day 0 -> 7 | Day 1 -> 8 | Day 2 -> 9 | Day 3 -> 10 |
# | Strip 0 |    0xx     |    x0x     |    xx0     |     xx9     |
# | Strip 1 |    1xx     |    x1x     |    xx1     |     xx0     |
# | Strip 2 |    2xx     |    x2x     |    xx2     |     xx1     |
# | Strip 3 |    3xx     |    x3x     |    xx3     |     xx2     |
# | Strip 4 |    4xx     |    x4x     |    xx4     |     xx3     |
# | Strip 5 |    5xx     |    x5x     |    xx5     |     xx4     |
# | Strip 6 |    6xx     |    x6x     |    xx6     |     xx5     |
# | Strip 7 |    7xx     |    x7x     |    xx7     |     xx6     |
# | Strip 8 |    8xx     |    x8x     |    xx8     |     xx7     |
# | Strip 9 |    9xx     |    x9x     |    xx9     |     xx8     |
def find_poisoned_bottle2(
    bottles: list[Bottle], strips: list[TestStrip]
) -> int:
    if len(bottles) > 1000 or len(strips) < 10:
        return -1

    tests = 4  # three digits, plus one extra
    n_test_strips = len(strips)

    # Run tests.
    for day in range(tests):
        run_test_set(bottles, strips, day)

    # Get results.
    previous_results = set()
    digits: list[int] = [0 for _ in range(tests)]
    for day in range(tests):
        result_day = day + TestStrip.DAYS_FOR_RESULT
        digits[day] = get_positive_on_day(strips, result_day, previous_results)
        previous_results.add(digits[day])

    # If day 1's results matched day 0's, update the digit.
    if digits[1] == -1:
        digits[1] = digits[0]

    # If day 2 matched day 0 or day 1, check day 3.
    # Day 3 is the same as day 2, but incremented by 1.
    if digits[2] == -1:
        if digits[3] == -1:  # Day 3 didn't give new result
            # Digit 2 equals digit 0 or digit 1.
            # But, digit 2, when incremented also matches digit 0 or digit 1.
            # This means that digit 0 incremented matches digit 1, or the other
            # way around.
            digits[2] = (
                digits[0]
                if ((digits[0] + 1) % n_test_strips) == digits[1]
                else digits[1]
            )
        else:
            digits[2] = (digits[3] - 1 + n_test_strips) % n_test_strips
    return digits[0] * 100 + digits[1] * 10 + digits[2]


# Run set of tests for this day.
def run_test_set2(
    bottles: list[Bottle], strips: list[TestStrip], day: int
) -> None:
    if day > 3:  # only works for 3 days (digits) + one extra
        return

    for bottle in bottles:
        index = get_test_strip_index_for_day(bottle, day, len(strips))
        test_strip = strips[index]
        test_strip.add_drop_on_day(day, bottle)


# Get strip that should be used on this bottle on this day.
def get_test_strip_index_for_day(
    bottle: Bottle, day: int, n_test_strips: int
) -> int:
    _id = bottle.get_id()
    match day:
        case 0:
            return _id // 100
        case 1:
            return (_id % 100) // 10
        case 2:
            return _id % 10
        case 2:
            return (_id % 10 + 1) % n_test_strips
        case _:
            return -1


# Get results that are positive for a particular day, excluding prior results.
def get_positive_on_day(
    test_strips: list[TestStrip], day: int, previous_results: set[int]
) -> int:
    for test_strip in test_strips:
        _id = test_strip.get_id()
        if test_strip.is_positive_on_day(day) and not (_id in previous_results):
            return test_strip.get_id()
    return -1


b = [Bottle(i + 1) for i in range(1000)]
b[random.randint(0, 1000)].set_as_poisoned()
s = [TestStrip(i) for i in range(10)]
print(find_poisoned_bottle2(b, s))


# Solution 3: Optimal Approach (7 days).
# This approach will work as long as 2ⁱ >= B, i is the number of test strips
# and B is the number of bottles.
def find_poisoned_bottle3(
    bottles: list[Bottle], strips: list[TestStrip]
) -> int:
    run_tests(bottles, strips)
    positive = get_positive_on_day3(strips, 7)
    return set_bits(positive)


# Add bottle contents to test strips
def run_tests(bottles: list[Bottle], test_strips: list[TestStrip]) -> None:
    for bottle in bottles:
        _id = bottle.get_id()
        bit_index = 0
        while _id > 0:
            if (_id & 1) == 1:
                test_strips[bit_index].add_drop_on_day(0, bottle)
            bit_index += 1
            _id >>= 1


# Get test strips that are positive on a particular day.
def get_positive_on_day3(test_strips: list[TestStrip], day: int) -> list[int]:
    positive = []
    for test_strip in test_strips:
        _id = test_strip.get_id()
        if test_strip.is_positive_on_day(day):
            positive.append(_id)
    return positive


# Create number by setting bits with indices specified in positive.
def set_bits(positive: list[int]) -> int:
    _id = 0
    for bit_index in positive:
        _id |= 1 << bit_index
    return _id


b = [Bottle(i + 1) for i in range(1000)]
b[random.randint(0, 1000)].set_as_poisoned()
s = [TestStrip(i) for i in range(10)]
print(find_poisoned_bottle3(b, s))


# My Solution. log n
def count_find_poison(
    poison_num: int, total_num: int = 1000, tester: int = 10
) -> int:
    bottles = [False for _ in range(total_num)]
    bottles[poison_num - 1] = True

    count = 0
    test_group = bottles
    while len(test_group) > 1:
        count += 1
        group_len = len(test_group) // tester if len(test_group) > tester else 1
        test_groups = []

        for i in range(tester):
            if i == tester - 1:
                test_groups.append(test_group[i * group_len :])
            else:
                test_groups.append(
                    test_group[i * group_len : (i + 1) * group_len]
                )
        for g in test_groups:
            if True in g:
                test_group = g
                break
        tester -= 1

    return count


print(count_find_poison(665))

# Solution.
# (1 + 2 + • • • + 20 = 20 * 21 / 2 = 210)
from decimal import Decimal


def get_heavy_bottle_num(
    weight: Decimal, bottle_1: Decimal, bottle_2: Decimal, bottle_count: int
):
    diff = bottle_2 - bottle_1
    result = (
        weight - Decimal(f"{bottle_count * (bottle_count + 1) / 2}")
    ) / diff
    return int(result)


print(
    get_heavy_bottle_num(Decimal("211.3"), Decimal("1.0"), Decimal("1.1"), 20)
)

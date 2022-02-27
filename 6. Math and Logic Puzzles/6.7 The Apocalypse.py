# Solution.
# Simulation
from decimal import Decimal
from random import randint


def run_n_families(n: int) -> Decimal:
    boys = 0
    girls = 0
    for i in range(n):
        genders = run_one_family()
        girls += genders[0]
        boys += genders[1]
    return Decimal(girls) / Decimal(boys + girls)


def run_one_family() -> tuple[int, int]:
    boys = 0
    girls = 0
    while girls == 0:  # until we have a girl
        if randint(0, 1):  # girl
            girls += 1
        else:  # boy
            boys += 1
    genders = (girls, boys)
    return genders

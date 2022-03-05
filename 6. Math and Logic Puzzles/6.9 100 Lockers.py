# Solution.
def test():
    rooms = [False for _ in range(100)]

    for i in range(1, 101):  # each pass
        for j in range(1, 101):  # lockers
            if j % i == 0:
                rooms[j - 1] = not rooms[j - 1]
                if rooms[j - 1]:
                    print(f"opened room {j}")
                else:
                    print(f"closed room {j}")
            else:
                continue
        print([i + 1 for i, val in enumerate(rooms) if val is True])
        print(f"----Pass {i} Ended----")


test()

# base definition
inf = int(1e9)


class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self, size: int):
        self.arr = [None for _ in range(size)]
        self.capacity = size
        self.top = -1

    def push(self, x):
        if self.is_full():
            raise FullStackException
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.is_empty():
            raise EmptyStackException
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if not self.is_empty():
            return self.arr[self.top]
        else:
            raise EmptyStackException

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1


# Solution 1.
# If we have a large stack, we waste a lot of space by keeping track of the min
# for every single element.
class NodeWithMin:
    def __init__(self, v: int, min_: int):
        self.value = v
        self.min = min_


class StackWithMin(Stack):
    def push(self, value: int):
        new_min = min(value, self.min())
        super().push(NodeWithMin(value, new_min))

    def min(self):
        if self.is_empty():
            return inf
        else:
            return self.peek().min


# Solution 2.
class StackWithMin2(Stack):
    def __init__(self, size):
        super().__init__(size)
        self.s2 = Stack(size)

    def push(self, value: int):
        if value <= self.min():
            self.s2.push(value)
        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.s2.pop()
        return value

    def min(self):
        if self.s2.is_empty():
            return inf
        else:
            return self.s2.peek()


# My Solution
class MyStack:
    def __init__(self, max_count: int):
        self.values = []
        self.max_count = max_count
        self.min_values = []
        self.top_idx = -1

    def push(self, value):
        if len(self.values) >= self.max_count:
            raise FullStackException
        self.values.append(value)
        if self.top_idx >= 0:
            self.min_values.append(min(self.min(), value))
        else:
            self.min_values.append(value)
        self.top_idx += 1
        print(f"push {value}")

    def pop(self) -> int:
        if len(self.values) <= 0:
            raise EmptyStackException
        self.min_values.pop()
        self.top_idx -= 1
        return self.values.pop()

    def min(self) -> int:
        if self.top_idx < 0:
            return inf
        return self.min_values[self.top_idx]


data = [9, 6, 4, 2, 5, 6, 1, 2]
# stack = MyStack(9)
stack = StackWithMin2(9)
for datum in data:
    stack.push(datum)
    print(stack.min())

for _ in range(len(data)):
    print(f"pop: {stack.pop()}")
    print(f"min: {stack.min()}")

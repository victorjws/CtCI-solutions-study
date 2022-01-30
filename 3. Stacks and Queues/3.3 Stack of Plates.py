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

    def __repr__(self):
        return f"Stack {self.arr}"

    def __len__(self):
        return self.top + 1

    def push(self, x):
        if self.is_full():
            raise FullStackException
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.is_empty():
            raise EmptyStackException
        value = self.arr[self.top]
        self.arr[self.top] = None
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


# Solution
class SetOfStacks:
    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity

    def __repr__(self):
        return f"SetOfStacks {self.stacks}"

    def push(self, v: int):
        last = self.get_last_stack()
        if last is not None and not last.is_full():  # add to last stack
            last.push(v)
        else:  # must create new stack
            _stack = Stack2(self.capacity)
            _stack.push(v)
            self.stacks.append(_stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            raise EmptyStackException
        v = last.pop()
        if len(last) == 0:
            self.stacks.pop()
        return v

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def pop_at(self, index: int):
        return self.left_shift(index, True)

    def left_shift(self, index: int, remove_top: bool):
        _stack = self.stacks[index]
        if remove_top:
            removed_item = _stack.pop()
        else:
            removed_item = _stack.remove_bottom()
        if _stack.is_empty():
            self.stacks.remove(_stack)
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            _stack.push(v)
        return removed_item


class Node:
    def __init__(self, v):
        self.value = v
        self.above = None
        self.below = None

    def __repr__(self):
        return f"Node {self.value}"


class Stack2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def __repr__(self):
        contents = []
        node = self.bottom
        while node is not None:
            contents.append(node)
            node = node.above
        return f"Stack {contents}"

    def is_full(self):
        return self.capacity == self.size

    def join(self, above, below):
        if below is not None:
            below.above = above
        if above is not None:
            above.below = below

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        t = self.top
        self.top = self.top.below
        self.top.above = None  # added for repr
        self.size -= 1
        return t.value

    def is_empty(self) -> bool:
        return self.size == 0

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom is not None:
            self.bottom.below = None
        self.size -= 1
        return b.value


# My Solution
class MySetOfStacks:
    def __init__(self, size: int):
        self.capacity = size
        self.stacks = []
        self.top = -1

    def __repr__(self):
        return f"SetOfStacks {self.stacks}"

    def push(self, value):
        if self.top % self.capacity == self.capacity - 1:
            self.stacks.append(Stack(self.capacity))
        self.stacks[-1].push(value)
        self.top += 1

    def pop(self):
        result = self.stacks[-1].pop()
        if self.top % self.capacity == 0:
            self.stacks.pop()
        self.top -= 1
        return result

    def pop_at(self, index: int):
        if self.top < index:
            raise IndexError
        _stack = self.stacks[index // self.capacity]
        temp = []
        for i in range(self.capacity - (index % self.capacity)):
            temp.append(_stack.pop())
        value = temp.pop()
        for i in range(len(temp)):
            _stack.push(temp.pop())
        self._trim(index)
        return value

    def _trim(self, index):
        start = self.stacks[index // self.capacity :]
        start.reverse()
        temp = []
        for _stack in start:
            for _ in range(len(_stack)):
                if (val := _stack.pop()) is not None:
                    temp.append(val)
        start.reverse()
        for _stack in start:
            for _ in range(_stack.capacity):
                if len(temp) <= 0:
                    break
                _stack.push(temp.pop())
        if self.stacks[-1].top < 0:
            self.stacks.pop()


data = [9, 6, 4, 2, 5, 6, 1, 2, 1]
# stack = MySetOfStacks(4)
stack = SetOfStacks(4)
for datum in data:
    stack.push(datum)

print(stack.pop_at(0))

# for _ in range(len(data)):
#     print(f"pop: {stack.pop()}")

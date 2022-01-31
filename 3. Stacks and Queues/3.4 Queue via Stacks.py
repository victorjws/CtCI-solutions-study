# base definition
class Node:
    def __init__(self, v):
        self.value = v
        self.above = None
        self.below = None

    def __repr__(self):
        return f"Node({self.value})"


class Stack:
    def __init__(self, capacity: int = 10):
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
        return f"Stack({contents})"

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
        if self.top is not None:
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

    def peek(self):
        return self.top


# Solution.
class MyQueue:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    @property
    def size(self):
        return self.stack_newest.size + self.stack_oldest.size

    def add(self, value):
        # Push onto stack_newest, which always has the newest elements on top
        self.stack_newest.push(value)

    def shift_stacks(self):
        # Move elements from stack_newest into stack_oldest.
        # This is usually done so that we can do operations on stack_oldest.
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()  # Ensure stack_oldest has the current elements
        return self.stack_oldest.peek()  # retrieve the oldest item.

    def remove(self):
        self.shift_stacks()  # Ensure stack_oldest has the current elements
        return self.stack_oldest.pop()  # pop the oldest item.


# My Solution
class MyQueueViaStacks:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.s1 = Stack(capacity)
        self.s2 = Stack(capacity)

    def __repr__(self):
        return f"Queue({self.s1})"

    def insert(self, v):
        self.s1.push(v)

    def remove(self):
        while self.s1.size > 1:
            self.s2.push(self.s1.pop())
        value = self.s1.pop()
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return value


data = [9, 6, 4, 2, 5, 6, 1, 2, 1]
stack = MyQueueViaStacks(len(data))
for datum in data:
    stack.insert(datum)


for _ in range(len(data)):
    print(stack.remove())

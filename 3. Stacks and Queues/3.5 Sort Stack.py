# base definition
inf = int(1e9)


class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self, size: int = 10):
        self.arr = [None for _ in range(size)]
        self.capacity = size
        self.top = -1

    def __repr__(self):
        return f"Stack ({self.arr})"

    def __len__(self):
        return self.size()

    def push(self, x):
        if self.is_full():
            raise FullStackException
        self.top += 1
        self.arr[self.top] = x

    def pop(self) -> int:
        if self.is_empty():
            raise EmptyStackException
        value = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return value

    def peek(self) -> int:
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


# Solution. O(N^2) time and O(N) space.
def sort(s):
    r = Stack()
    while not s.is_empty():
        # Insert each element in s in sorted order into r.
        tmp = s.pop()
        while not r.is_empty() and r.peek() > tmp:
            s.push(r.pop())
        r.push(tmp)

    # Copy the elements from r back into s.
    while not r.is_empty():
        s.push(r.pop())


# My Solution
class SortedStack:
    def __init__(self, capacity: int):
        self.primary_stack = Stack(capacity)
        self.secondary_stack = Stack(capacity)

    def __repr__(self):
        return f"SortedStack (first:{self.primary_stack}, second:{self.secondary_stack})"

    def push(self, v):
        self.primary_stack.push(v)

    def sort(self):
        while not self.primary_stack.is_empty():
            value = self.primary_stack.pop()
            while (
                not self.secondary_stack.is_empty()
                and self.secondary_stack.peek() > value
            ):
                self.primary_stack.push(self.secondary_stack.pop())
            self.secondary_stack.push(value)
        while not self.secondary_stack.is_empty():
            self.primary_stack.push(self.secondary_stack.pop())


# With the merge sort solution.
def merge_sort(s):
    if s.size() == 1:
        return s
    half = s.size() // 2
    left_s = Stack(len(s))
    right_s = Stack(len(s))
    for _ in range(half):
        left_s.push(s.pop())
    while not s.is_empty():
        right_s.push(s.pop())
    left_partition = merge_sort(left_s)
    right_partition = merge_sort(right_s)

    return merge(left_partition, right_partition)


def merge(left, right):
    s = Stack(len(left) + len(right))
    while not left.is_empty() or not right.is_empty():
        if left.is_empty():
            s.push(right.pop())
        elif right.is_empty():
            s.push(left.pop())
        elif left.peek() > right.peek():
            s.push(right.pop())
        else:
            s.push(left.pop())
    result = Stack(len(left) + len(right))
    while not s.is_empty():
        result.push(s.pop())
    return result


# With the quick sort solution.
def quick_sort(s):
    if len(s) <= 1:
        return s
    left = Stack(len(s))
    right = Stack(len(s))
    pivot = s.pop()
    while not s.is_empty():
        value = s.pop()
        if value < pivot:
            left.push(value)
        else:
            right.push(value)
    left_partition = quick_sort(left)
    right_partition = quick_sort(right)

    return merge_quick(left_partition, pivot, right_partition)


def merge_quick(left, pivot, right):
    s = Stack()
    while not left.is_empty():
        s.push(left.pop())
    s.push(pivot)
    while not right.is_empty():
        s.push(right.pop())
    result = Stack(len(s))
    while not s.is_empty():
        result.push(s.pop())
    return result


data = [9, 6, 4, 2, 5, 6, 1, 2]
# stack = SortedStack(len(data))
stack = Stack(len(data))
for datum in data:
    stack.push(datum)
# stack.sort()
# print(merge_sort(stack))
print(quick_sort(stack))

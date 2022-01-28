# Solution: Fixed Division
class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class FixedMultiStack:
    number_of_stacks: int = 3
    stack_capacity: int
    values: list[int]
    sizes: list[int]

    def __init__(self, stack_size: int):
        self.stack_capacity = stack_size
        self.values = [0 for _ in range(stack_size * self.number_of_stacks)]
        self.sizes = [0 for _ in range(self.number_of_stacks)]

    # Push value onto stack
    def push(self, stack_num: int, value: int) -> None:
        # Check that we have space for the next element
        if self.is_full(stack_num):
            raise FullStackException

        # Increment stack pointer and then update top value.from
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    # Pop item from top stack.
    def pop(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            raise EmptyStackException

        top_index: int = self.index_of_top(stack_num)
        value: int = self.values[top_index]  # Get top
        self.values[top_index] = 0  # Clear
        self.sizes[stack_num] -= 1  # Shrink
        return value

    # Return top element.
    def peek(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            raise EmptyStackException
        return self.values[self.index_of_top(stack_num)]

    # Return if stack is empty.
    def is_empty(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == 0

    # Return if stack is full.
    def is_full(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == self.stack_capacity

    # Return index of the top of the stack.
    def index_of_top(self, stack_num: int) -> int:
        offset: int = stack_num * self.stack_capacity
        size: int = self.sizes[stack_num]
        return offset + size - 1


# Solution 2: Flexible Divisions
class MultiStack:
    info: list["StackInfo"]
    values: list[int]

    # StackInfo is a simple class that holds a set of data about each stack.
    # It does not hold the actual items in the stack.
    # We could have done this with just a bunch of individual variables, but
    # that's messy and doesn't gain us much.
    class StackInfo:
        start: int
        size: int
        capacity: int

        def __init__(self, start: int, capacity: int):
            self.start = start
            self.capacity = capacity

        # Check if an index on the full array is within the stack boundaries.
        # The stack can wrap around to the start of the array.
        def is_within_stack_capacity(self, index: int) -> bool:
            # If outside of bounds of array, return false.
            if index < 0 or index >= len(self.values):
                return False

            # If index wraps around, adjust it.
            contiguous_index: int = (
                index + len(self.values) if index < self.start else index
            )
            end: int = self.start + self.capacity
            return self.start < contiguous_index < self.end

        def last_capacity_index(self) -> int:
            return self.adjust_index(self.start + self.capacity - 1)

        def last_element_index(self) -> int:
            return self.adjust_index(self.start + self.size - 1)

        def is_full(self) -> bool:
            return self.size == self.capacity

        def is_empty(self) -> bool:
            return self.size == 0

    def __init__(self, number_of_stacks: int, default_size: int):
        # Create metadata for all the stacks.
        self.info = [
            self.StackInfo(default_size * i, default_size)
            for i in range(number_of_stacks)
        ]
        self.values = [0 for _ in range(number_of_stacks * default_size)]

    # Push value onto stack num, shifting/expanding stacks as necessary.
    # Throws exception if all stacks are full.
    def push(self, stack_num: int, value: int) -> None:
        if self.all_stacks_are_full():
            raise FullStackException

        # If this stack is full, expand it.
        stack = self.info[stack_num]
        if stack.is_full():
            self.expand(stack_num)

        # Find the index of the top element in the array + 1 , and increment
        # the stack pointer
        stack.size += 1
        self.values[stack.last_element_index()] = value

    # Remove value from stack.
    def pop(self, stack_num) -> int:
        stack = self.info[stack_num]
        if stack.is_empty():
            raise EmptyStackException

        # Remove last element.
        value = self.values[stack.last_element_index()]
        self.values[stack.last_element_index()] = 0  # Clear item
        stack.size -= 1  # Shrink size
        return value

    # Get top element of stack.
    def peek(self, stack_num) -> int:
        stack = self.info[stack_num]
        return self.values[stack.last_element_index()]

    # Shift items in stack over by one element.
    # If we have available capacity, then we'll end up shrinking the stack by
    # one element.
    # If we don't have available capacity, then we'll need to shift the next
    # stack over too.
    def shift(self, stack_num: int) -> None:
        print("/// Shifting" + stack_num)
        stack = self.info[stack_num]

        # If this stack is at its full capacity, then you need to move the next
        # stack over by one element. This stack can now claim teh freed index.
        if stack.size >= stack.capacity:
            next_stack = stack_num + 1 % len(self.info)
            self.shift(next_stack)
            stack.capacity += 1  # claim index that next stack lost

        # Shift all elements in stack over by one.
        index: int = stack.last_capacity_index()
        while stack.is_within_stack_capacity(index):
            self.values[index] = self.values[self.previous_index(index)]
            index = self.previous_index(index)

        # Adjust stack data.
        self.values[stack.start] = 0  # Clear item
        stack.start = self.next_index(stack.start)  # move start
        stack.capacity -= 1  # Shrink capacity

    # Expand stack by shifting over other stacks.
    def expand(self, stack_num) -> None:
        self.shift((stack_num + 1) % len(self.info))
        self.info[stack_num].capacity += 1

    # Returns the number of items actually present in stack.
    def number_of_elements(self) -> int:
        size = 0
        for sd in self.info:
            size += sd.size
        return size

    # Returns true is all the stacks are full.
    def all_stacks_are_full(self) -> bool:
        return self.number_of_elements() == len(self.values)

    # Adjust index to be within the range of 0 -> length - 1.
    def adjust_index(self, index: int) -> int:
        # Java's mod operator can return neg values.
        # (since we're wrapping around the index).
        max_: int = len(self.values)
        return ((index % max_) + max_) % max_

    # Get index after this index, adjusted for wrap around.
    def next_index(self, index: int) -> int:
        return self.adjust_index(index + 1)

    # Get index before this index, adjusted for wrap around.
    def previous_index(self, index: int) -> int:
        return self.adjust_index(index - 1)

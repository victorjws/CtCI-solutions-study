# Solution
def partition(node: "Node", x: int) -> "Node":
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    # Partition list
    while node is not None:
        next = node.next
        node.next = None
        if node.data < x:
            # Insert node into end of before list
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            # Insert node into end of after list
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = next

    if before_start is None:
        return after_start

    # Merge before list and after list
    before_end.next = after_start
    return before_start


# Simpler Solution.
# If we don't care about making the elements of the list 'stable'.
def partition2(node: "Node", x: int) -> "Node":
    head = node
    tail = node

    while node is not None:
        next = node.next
        if node.data < x:
            # Insert node at head.
            node.next = head
            head = node
        else:
            # Insert node at tail.
            tail.next = node
            tail = node
        node = next
    tail.next = None

    # The head has changed, so we need to return it to the user.
    return head


# My Solution
class Node:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


def partitioning(node: Node, partition: int):
    p1 = node
    p2 = node.next
    while p1 is not None and p2 is not None:
        if p2.data >= partition:
            p2 = p2.next
            continue
        if p1.data < partition:
            p1 = p1.next
            continue
        p1.data, p2.data = p2.data, p1.data
        p1 = p1.next
        p2 = p2.next


K = int(input())
input_values = [int(i) for i in input().split()]
prev = h = Node(input_values[0])
for i in input_values[1:]:
    n = Node(i)
    prev.next = n
    prev = n
# partitioning(h, K)
h = partition2(h, K)
n = h
while n is not None:
    print(n.data)
    n = n.next

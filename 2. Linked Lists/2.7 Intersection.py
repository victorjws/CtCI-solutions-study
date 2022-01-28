# base definition
class Node:
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


# Solution. O(A+B) time, A and B are the lengths of the two linked lists.
#           O(1) additional space.
def find_intersection(list1: Node, list2: Node) -> Node | None:
    if list1 is None or list2 is None:
        return None

    # Get tail and sizes.
    result1 = get_tail_and_size(list1)
    result2 = get_tail_and_size(list2)

    # If different tail nodes, then there's no intersection.
    if result1.tail != result2.tail:
        return None

    # Set pointers to the start of each linked list.
    shorter = list1 if result1.size < result2.size else list2
    longer = list2 if result1.size < result2.size else list1

    # Advance the pointer for the longer linked list by difference in lengths.
    longer = get_kth_node(longer, abs(result1.size - result2.size))

    # Move both pointers until you have a collision.
    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next

    # Return either one.
    return longer


class Result:
    def __init__(self, tail: Node, size: int):
        self.tail = tail
        self.size = size


def get_tail_and_size(lst: Node) -> Result | None:
    if lst is None:
        return None

    size: int = 1
    current: Node = lst
    while current.next is not None:
        size += 1
        current = current.next
    return Result(current, size)


def get_kth_node(head: Node, k: int) -> Node | None:
    current: Node = head
    while k > 0 and current is not None:
        current = current.next
        k -= 1
    return current


# My Solution
def intersection(l1, l2):
    l1_len = get_length(l1)
    l2_len = get_length(l2)

    if l1_len >= l2_len:
        longer = l1
        shorter = l2
    else:
        longer = l2
        shorter = l1
    diff = abs(l1_len - l2_len)

    for _ in range(diff):
        longer = longer.next

    while longer is not None:
        if longer is shorter:
            if longer.next is None:
                return True
        longer = longer.next
        shorter = shorter.next
    return False


def get_length(head) -> int:
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


l1_ = n1 = Node(1)
l2_ = n2 = Node(2)
for i in range(10):
    n1.next = n = Node(i)
    n1 = n1.next
    if i == 5:
        n2.next = n
        # n2 = n2.next
print(intersection(l1_, l2_))

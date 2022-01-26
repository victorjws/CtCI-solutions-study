# Solution
from typing import Optional


def add_list(l1: "Node", l2: "Node", carry: int) -> Optional["Node"]:
    if l1 is None and l2 is None and carry == 0:
        return None

    result = Node()
    value = carry
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data
    result.data = value % 10  # Second digit of number

    # Recurse
    if l1 is not None or l2 is not None:
        more = add_list(
            None if l1 is None else l1.next,
            None if l2 is None else l2.next,
            1 if value >= 10 else 0,
        )
        result.next = more
    return result


# Follow Up Solution
class PartialSum:
    sum: Optional["Node"] = None
    carry: int = 0


def add_lists(l1: "Node", l2: "Node") -> "Node":
    len1 = get_length(l1)
    len2 = get_length(l2)

    # Pad the shorter list with zeros
    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)

    # Add lists
    sum = add_lists_helper(l1, l2)

    # If there was a carry value left over, insert this at the front of the
    # list. Otherwise, just return the linked list.
    if sum.carry == 0:
        return sum.sum
    else:
        result = insert_before(sum.sum, sum.carry)
        return result


def add_lists_helper(l1: "Node", l2: "Node") -> PartialSum:
    if l1 is None and l2 is None:
        sum: PartialSum = PartialSum()
        return sum
    # Add smaller digits recursively
    sum = add_lists_helper(l1.next, l2.next)

    # Add carry to current data
    val = sum.carry + l1.data + l2.data

    # Insert sum of current digits
    full_result = insert_before(sum.sum, val % 10)

    # Return sum so far, and the carry value
    sum.sum = full_result
    sum.carry = val // 10
    return sum


# Pad the list with zeros
def pad_list(l: "Node", padding: int) -> "Node":
    head = l
    for i in range(padding):
        head = insert_before(head, 0)
    return head


# Helper function to insert node in the front of a linked list
def insert_before(lst: "Node", data: int) -> "Node":
    node = Node(data)
    if lst is not None:
        node.next = lst
    return node


def get_length(node: "Node") -> int:
    length = 0
    pointer = node
    while pointer is not None:
        length += 1
        pointer = pointer.next
    return length


# My Solution
class Node:
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


def sum_list(
    operand1: Optional[Node],
    operand2: Optional[Node],
    result: Optional[Node] = None,
    carry: int = 0,
):
    x = operand1.data if operand1 is not None else 0
    y = operand2.data if operand2 is not None else 0

    _result = x + y + carry

    if _result >= 10:
        _carry = 1
        _result %= 10
    else:
        _carry = 0

    n = Node(_result)
    if result is None:
        result = n
    else:
        result.next = n
        result = result.next

    n_operand1 = operand1.next if operand1 is not None else None
    n_operand2 = operand2.next if operand2 is not None else None

    if (n_operand1 is not None) or (n_operand2 is not None) or _carry != 0:
        sum_list(operand1.next, operand2.next, result, _carry)

    return result


op1 = [int(i) for i in input().split()]
op2 = [int(i) for i in input().split()]
# op1.reverse()
# op2.reverse()
prev = opl1 = Node(op1[0])
for i in op1[1:]:
    n = Node(i)
    prev.next = n
    prev = n
prev = opl2 = Node(op2[0])
for i in op2[1:]:
    n = Node(i)
    prev.next = n
    prev = n
# n = sum_list(opl1, opl2)
n = add_lists(opl1, opl2)
while n is not None:
    print(n.data)
    n = n.next


# My Follow Up Solution
# def sum_forward_list(l1, l2):
#     l1_length = get_length(l1)
#     l2_length = get_length(l2)
#     if l1_length > l2_length:
#         longer = l1
#         shorter = l2
#         longer_length = l1_length
#         shorter_length = l2_length
#     else:
#         longer = l2
#         shorter = l1
#         longer_length = l2_length
#         shorter_length = l1_length
#
#     if longer_length != shorter_length:
#         diff = longer_length - shorter_length
#         for _ in range(diff):
#             n = Node(0)
#             n.next = shorter
#             shorter = n

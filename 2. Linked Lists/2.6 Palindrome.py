# base definition
class Node:
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


# Solution 1: Reverse and Compare
def is_palindrome1(head: Node) -> bool:
    reversed_ = reverse_and_clone(head)
    return is_equal(head, reversed_)


def reverse_and_clone(node: Node) -> Node:
    head = None
    while node is not None:
        n = Node(node.data)  # Clone
        n.next = head
        head = n
        node = node.next
    return head


def is_equal(one: Node, two: Node) -> bool:
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next
    return one is None and two is None


# Solution 2: Iterative Approach
def is_palindrome(head: Node) -> bool:
    fast = head
    slow = head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()

        if top != slow.data:
            return False
        slow = slow.next
    return True


# Solution 3: Recursive Approach
class Result:
    def __init__(self, node: Node = None, result: bool = None):
        self.node = node
        self.result = result


def is_palindrome2(head: Node) -> bool:
    length = length_of_list(head)
    p = is_palindrome_recurse(head, length)
    return p.result


def is_palindrome_recurse(head: Node, length: int) -> Result:
    if head is None or length <= 0:  # Even number of nodes
        return Result(head, True)
    elif length == 1:  # Odd number of nodes
        return Result(head.next, True)

    # Recurse on sublist.
    res = is_palindrome_recurse(head.next, length - 2)

    # If child calls are not a palindrome, pass back up a failure.
    if not res.result or res.node is None:
        return res

    # Check if matches corresponding node on other side.
    res.result = head.data == res.node.data

    # Return corresponding node.
    res.node = res.node.next

    return res


def length_of_list(n_: Node) -> int:
    size = 0
    while n_ is not None:
        size += 1
        n_ = n_.next
    return size


# My Solution
def is_palindrome_(head: Node, length: int) -> bool:
    stack = []
    middle = length // 2
    node = head
    for _ in range(middle):
        stack.append(node)
        node = node.next
    if length % 2 != 0:
        node = node.next

    node_2 = node
    while stack:
        node_1 = stack.pop()
        if not node_2.data == node_1.data:
            return False
        node_2 = node_2.next
    return True


L = int(input())
nodes = [int(i) for i in input().split()]
prev = None
h = None
for i in nodes:
    n = Node(i)
    if prev is None:
        h = n
    else:
        prev.next = n
    prev = n

print(is_palindrome_(h, L))

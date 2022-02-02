# base definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


# Solution 1: In-Order Traversal. Only works no duplicate values.
index = 0


def copy_bst(root: Node, array: list[int]):
    global index
    if root is None:
        return
    copy_bst(root.left, array)

    array.append(root.value)

    copy_bst(root.right, array)


def check_bst(root: Node):
    array = []
    copy_bst(root, array)
    for i in range(1, len(array)):
        if array[i] <= array[i - 1]:
            return False
    return True


# Solution 1-1: without array
last_printed = None


class WrapInt:  # instead of last_printed.
    def __init__(self):
        self.value = None


def check_bst2(n: Node):
    global last_printed

    if n is None:
        return True

    # Check / recurse left
    if not check_bst2(n.left):
        return False

    # Check current
    if last_printed is not None and n.value <= last_printed:
        return False

    last_printed = n.value

    # Check /recurse right
    if not check_bst2(n.right):
        return False

    return True  # All good!


# Solution 2: The Min / Max Solution.
# O(N) time. N = number of nodes in the tree.
# O(log N) space.
def check_bst3(n: Node, minimum: int = None, maximum: int = None):
    if n is None:
        return True
    if (minimum is not None and n.value <= minimum) or (
        maximum is not None and n.value > maximum
    ):
        return False
    if (not check_bst3(n.left, minimum, n.value)) or (
        not check_bst3(n.right, n.value, maximum)
    ):
        return False
    return True


# My Solution.
MIN_VALUE = int(-1e9)
MAX_VALUE = int(1e9)


def my_check_bst(
    node, minimum: int = None, maximum: int = None
) -> tuple[int, int, bool]:
    if minimum is None and maximum is None:
        minimum = MIN_VALUE
        maximum = MAX_VALUE

    if node.left:
        minimum, _, result = my_check_bst(node.left, minimum, node.value)
        if not result:
            return -1, -1, False
    if node.right:
        _, maximum, result = my_check_bst(node.right, node.value, maximum)
        if not result:
            return -1, -1, False

    if minimum <= node.value < maximum:
        return minimum, maximum, True
    else:
        return -1, -1, False


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node5.left = node3
node5.right = node7
node3.left = node1
node3.right = node4
node1.left = node0
node1.right = node2
node7.left = node6
node7.right = node8
node6.right = node9
print(my_check_bst(node5))

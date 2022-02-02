# base definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


# Not very efficient Solution.
# O(N log N) since each node is 'touched' once per node above it.
def get_height(root: Node) -> int:
    if root is None:  # Base case
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root: Node) -> bool:
    if root is None:  # Base case
        return True

    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:  # Recurse
        return is_balanced(root.left) and is_balanced(root.right)


# Solution. O(N) time and O(H) space, where  H is the height of the tree.
MIN_VALUE = int(-1e10)


def check_height(root: Node) -> int:
    if root is None:
        return -1

    left_height = check_height(root.left)
    if left_height == MIN_VALUE:
        return MIN_VALUE  # Pass error up

    right_height = check_height(root.right)
    if right_height == MIN_VALUE:
        return MIN_VALUE  # Pass error up

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return MIN_VALUE  # Found error -> pass it back
    else:
        return max(left_height, right_height) + 1


def is_balanced2(root: Node) -> bool:
    return check_height(root) != MIN_VALUE


# My Solution
class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root
        ret = "  " * level + repr(node) + "\n"
        if node is not None or level == 0:
            ret += self.__repr__(node.left, level + 1)
            ret += self.__repr__(node.right, level + 1)
        return ret


def my_check_height(node, level=0):
    if node is None:
        return level
    left = my_check_height(node.left, level + 1)
    right = my_check_height(node.right, level + 1)
    if level == 0:
        return abs(left - right) <= 1
    return max(left, right)


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
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node3.left = node7
node3.right = node8
node7.left = node9
t = Tree()
t.root = node0
print(t)
print(my_check_height(node0))

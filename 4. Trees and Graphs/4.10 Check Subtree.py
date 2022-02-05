# base definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"Node({self.value})"

    def set_left(self, n):
        self.left = n
        n.parent = self

    def set_right(self, n):
        self.right = n
        n.parent = self


# Solution.
# O(n + m) time and O(n + m) space, where n and m are the number of nodes in T1
# and T2, respectively.
def contains_tree(t1: Node, t2: Node) -> bool:
    string1 = ""
    string2 = ""

    get_order_string(t1, string1)
    get_order_string(t2, string2)

    return string1.find(string2) != -1


def get_order_string(node: Node, sb: str):
    if node is None:
        sb += "X"  # Add null indicator
        return

    sb += f"{node.value} "  # Add root
    get_order_string(node.left, sb)  # Add left
    get_order_string(node.right, sb)  # Add right


# Solution 2: The Alternative Approach.
# O(n + km) time, where k is the number of occurrences of T2's root in T1.
# O(log(n) + log(m)) memory
def contains_tree2(t1: Node, t2: Node) -> bool:
    if t2 is None:
        return True  # The empty tree is always a subtree
    return sub_tree(t1, t2)


def sub_tree(r1: Node, r2: Node) -> bool:
    if r1 is None:
        return False  # big tree empty & subtree still not found.
    elif r1.value == r2.value and match_tree(r1, r2):
        return True
    return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)


def match_tree(r1: Node, r2: Node) -> bool:
    if r1 is None and r2 is None:
        return True  # nothing left in the subtree
    elif r1 is None or r2 is None:
        return False  # exactly tree is empty, therefore trees don't match
    elif r1.value != r2.value:
        return False  # data doesn't match
    else:
        return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)


# My Solution.
def my_preorder_traversal(node: Node, result: str) -> str:
    if node is None:
        result += "N "
        return result

    result += f"{node.value} "
    result = my_preorder_traversal(node.left, result)
    result = my_preorder_traversal(node.right, result)
    return result


def my_check_subtree(t1: Node, t2: Node) -> bool:
    t1_traversal = my_preorder_traversal(t1, "")
    t2_traversal = my_preorder_traversal(t2, "")
    return t2_traversal in t1_traversal


# My Solution 2.
def my_check_subtree2(t1: Node, t2: Node) -> bool:
    t1 = find_target(t1, t2)
    return check_tree_is_identical(t1, t2)


def find_target(node: Node, target: Node) -> Node | None:
    if node is None:
        return None
    elif node.value == target.value:
        return node

    left = find_target(node.left, target)
    if left:
        return left
    right = find_target(node.right, target)
    if right:
        return right
    return None


def check_tree_is_identical(t1: Node, t2: Node) -> bool:
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.value != t2.value:
        return False

    left = check_tree_is_identical(t1.left, t2.left)
    right = check_tree_is_identical(t1.right, t2.right)
    if left and right:
        return True
    return False


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
node10 = Node(10)
node7.set_left(node3)
node7.set_right(node8)
node3.set_left(node1)
node3.set_right(node6)
node1.set_left(node0)
node1.set_right(node2)
node6.set_left(node5)
node5.set_left(node4)
node8.set_right(node9)
node9.set_right(node10)
node3_1 = Node(3)
node1_1 = Node(1)
node6_1 = Node(6)
node3_1.set_left(node1_1)
node3_1.set_right(node6_1)
# print(my_check_subtree(node7, node9))
print(my_check_subtree2(node7, node3_1))

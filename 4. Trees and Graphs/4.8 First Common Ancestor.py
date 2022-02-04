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


# Solution 1: With Links to Parents.
# O(d) time, where d is the depth of the deeper node.
def common_ancestor(p: Node, q: Node) -> Node:
    delta = depth(p) - depth(q)  # get difference in depths
    first = q if delta > 0 else p  # get shallower node
    second = p if delta > 0 else q  # get deeper node
    second = go_up_by(second, abs(delta))  # move deeper node up

    # Find where paths intersect
    while first != second and first is not None and second is not None:
        first = first.parent
        second = second.parent
    return None if first is None or second is None else first


def go_up_by(node: Node, delta: int) -> Node:
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


def depth(node: Node) -> int:
    dep = 0
    while node is not None:
        node = node.parent
        dep += 1
    return dep


# Solution 2: With Links to Parent(Better Worst-Case Runtime)
# O(t) time, where t is the size of the subtree for the first common ancestor.
# In the worst case, this will be O(n), where n is the number of nodes in the
# tree.
def common_ancestor2(root: Node, p: Node, q: Node) -> Node | None:
    # Check if either node is not in the tree, or if one covers the other.
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    # Traverse upwards until you find a node that covers q.
    sibling = get_sibling(p)
    parent = p.parent
    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


def covers(root: Node, p: Node) -> bool:
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


def get_sibling(node: Node) -> Node | None:
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.right if parent.left == node else parent.left


# Solution 3: Without Links to Parents
# O(n) time on a balanced tree.
def common_ancestor3(root: Node, p: Node, q: Node) -> Node | None:
    # Error check - one node is not in the tree.
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestor_helper(root, p, q)


def ancestor_helper(root: Node, p: Node, q: Node) -> Node | None:
    if root is None or root == p or root == q:
        return root

    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if p_is_on_left != q_is_on_left:  # Nodes are on different side
        return root
    child_side = root.left if p_is_on_left else root.right
    return ancestor_helper(child_side, p, q)


# Solution 4: Optimized
#      3
#    /  \
#   1    5
#         \
#          8
# common_ancestor(node3, node 5, node7)  # -> 5
#   calls common_ancestor(node1, node 5, node7)  # -> None
#     calls common_ancestor(node5, node 5, node7)  # -> 5
#       calls common_ancestor(node8, node 5, node7)  # -> None
class Result:
    def __init__(self, n: Node | None, is_anc: bool):
        self.node = n
        self.is_ancestor = is_anc


def common_ancestor4(root: Node, p: Node, q: Node) -> Node | None:
    r = common_anc_helper(root, p, q)
    if r.is_ancestor:
        return r.node
    return None


def common_anc_helper(root: Node, p: Node, q: Node) -> Result:
    if root is None:
        return Result(None, False)

    if root == p and root == q:
        return Result(root, True)

    rx = common_anc_helper(root.left, p, q)
    if rx.is_ancestor:  # Found common ancestor
        return rx

    ry = common_anc_helper(root.right, p, q)
    if ry.is_ancestor:  # Found common ancestor
        return ry

    if rx.node is not None and ry.node is not None:
        return Result(root, True)  # This is the common ancestor
    elif root == p or root == q:
        # If we're currently at p or q, and we also found one of those nodes in
        # a subtree, then this is truly an ancestor and the flag should be true.
        is_ancestor = rx.node is not None or ry.node is not None
        return Result(root, is_ancestor)
    else:
        return Result(rx.node if rx.node is not None else ry.node, False)


# My Solution.
def my_first_common_ancestor(node: Node, p: Node, q: Node) -> Node | None:
    if node is None:
        return None
    elif node == p:
        return p
    elif node == q:
        return q

    left = my_first_common_ancestor(node.left, p, q)
    right = my_first_common_ancestor(node.right, p, q)

    if (left == p and right == q) or (right == p and left == q):
        return node
    return left or right


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
print(my_first_common_ancestor(node7, node4, node2))

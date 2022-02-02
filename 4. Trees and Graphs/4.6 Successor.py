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
def inorder_succ(n: Node) -> Node | None:
    if n is None:
        return None

    # Found right children -> return leftmost node of right subtree.
    if n.right is not None:
        return left_most_child(n.right)
    else:
        q = n
        x = q.parent
        # Go up until we're on left instead of right
        while x is not None and x.left != q:
            q = x
            x = x.parent
        return x


def left_most_child(n: Node):
    if n is None:
        return None
    while n.left is not None:
        n = n.left
    return n


# My Solution.
def find_next_node(node: Node) -> Node | None:
    if node is None:
        return None
    if node.right:
        n = node.right
        while n.left is not None:
            n = n.left
        return n
    parent = node.parent
    child = node
    while parent.right == child:
        child = parent
        parent = parent.parent
        if parent is None:
            return None
    return parent


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
print(find_next_node(node3))

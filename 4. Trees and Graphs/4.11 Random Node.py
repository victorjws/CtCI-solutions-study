# base definition
import random


# Solution.
# Option 6. (Fast & Working)
class TreeNode:
    def __init__(self, d: int):
        self.data = d
        self.size = 1
        self.left: "TreeNode" = None
        self.right: "TreeNode" = None

    def get_random_node(self) -> "TreeNode":
        left_size = 0 if self.left is None else self.left.size
        index = random.randint(0, self.size)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert_in_order(self, d: int):
        if d <= self.data:
            if self.left is None:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1

    def find(self, d: int) -> "TreeNode":
        if d == self.data:
            return self
        elif d <= self.data:
            return self.left.find(d) if self.left is not None else None
        elif d > self.data:
            return self.right.find(d) if self.right is not None else None
        return None


# Option 7. (Fast & Working)
#   O(log N) time in a balanced tree.
#   We can also describe the runtime as O(D), where D is the max depth of the
#   tree.
#   Note that O(D) is an accurate description of the runtime whether the tree
#   is balanced or not.
class TreeNode2:
    def __init__(self, d: int):
        # same
        self.data = d
        self.size = 1
        self.left: "TreeNode2" = None
        self.right: "TreeNode2" = None

    def __repr__(self):
        return f"Node({self.data})"

    def get_ith_node(self, i: int) -> "TreeNode2":
        left_size = 0 if self.left is None else self.left.size
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            # Skipping over left_size + 1 nodes, so subtract them.
            return self.right.get_ith_node(i - (left_size + 1))

    def insert_in_order(self, d: int):
        # same
        if d <= self.data:
            if self.left is None:
                self.left = TreeNode2(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = TreeNode2(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1

    def find(self, d: int) -> "TreeNode2":
        # same
        if d == self.data:
            return self
        elif d <= self.data:
            return self.left.find(d) if self.left is not None else None
        elif d > self.data:
            return self.right.find(d) if self.right is not None else None
        return None


class Tree:
    root: TreeNode2 = None

    def __repr__(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root
        ret = "  " * level + repr(node) + "\n"
        if node is not None or level == 0:
            ret += self.__repr__(node.left, level + 1)
            ret += self.__repr__(node.right, level + 1)
        return ret

    def size(self) -> int:
        return 0 if self.root is None else self.root.size

    def get_random_node(self) -> TreeNode2 | None:
        if self.root is None:
            return None

        i = random.randint(0, self.size())
        return self.root.get_ith_node(i)

    def insert_in_order(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode2(value)
        else:
            self.root.insert_in_order(value)


tree = Tree()
tree.insert_in_order(7)
tree.insert_in_order(5)
tree.insert_in_order(15)
tree.insert_in_order(3)
tree.insert_in_order(7)
tree.insert_in_order(12)
tree.insert_in_order(12)
tree.insert_in_order(17)
tree.insert_in_order(2)
tree.insert_in_order(4)
tree.insert_in_order(6)
tree.insert_in_order(8)
tree.insert_in_order(1)
tree.insert_in_order(9)
print(tree.get_random_node())


# My Solution.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.child_count = 0

    def __repr__(self):
        return f"Node({self.value})"

    def set_left(self, n):
        self.left = n
        n.parent = self

    def set_right(self, n):
        self.right = n
        n.parent = self


class Tree2:
    def __init__(self, root: Node):
        self.root = root
        self.total_count = 1

    def insert(self, value: int):
        self.total_count += 1
        parent = None
        node = self.root
        while node is not None:
            node.child_count += 1
            parent = node
            if node.value >= value:
                node = node.left
            else:
                node = node.right
        if parent.value >= value:
            parent.set_left(Node(value))
        else:
            parent.set_right(Node(value))

    def find(self, value: int) -> Node | None:
        node = self.root
        while node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return node

    def delete(self, value: int):
        pass
        # node = self.find(value)
        # while node.left is not None:

    def get_random_node(self) -> Node:
        node = self.root
        ran_int = random.randrange(0, node.child_count)
        while True:

            if ran_int == 0:
                return node

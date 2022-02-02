# base definition
from collections import defaultdict, deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


# DFS Solution. O(N) time.
# This use more O(logN) extra space than BFS,
# but both solutions require returning O(N) data.
# So they are equally efficient when it comes to 'big O'.
def create_level_linked_list(root: Node, lists: list[list[Node]], level: int):
    if root is None:  # base case
        return
    lst = None
    if len(lists) == level:  # Level not contained in list
        lst = []
        # Levels are always traversed in order.
        # So, if this is the first time we've visited level i, we must have
        # seen levels 0 through i -1.
        # We can therefore safely add the level at the end.
        lists.append(lst)
    else:
        lst = lists[level]
    lst.append(root)
    create_level_linked_list(root.left, lists, level + 1)
    create_level_linked_list(root.right, lists, level + 1)
    return lists


# BFS Solution. O(N) time.
def create_level_linked_list_bfs(root: Node):
    result = []
    # "Visit" the root
    current = []
    if root is not None:
        current.append(root)
    while len(current) > 0:
        result.append(current)  # Add previous level
        parents = current  # Go to next level
        for parent in parents:
            # Visit the children
            if parent.left is not None:
                current.append(parent.left)
            if parent.right is not None:
                current.append(parent.right)
    return result


# My Solution.
class MyTree:
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


def my_get_lists_from_tree(tree):
    q = deque([(tree.root, 0)])
    table = defaultdict(list)
    while q:
        node, level = q.popleft()
        table[level].append(node)
        if node.left is not None:
            q.append((node.left, level + 1))
        if node.right is not None:
            q.append((node.right, level + 1))
    return table


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
g = MyTree()
g.root = node0
# print(my_get_lists_from_tree(g))
print(create_level_linked_list(g.root, [], 0))

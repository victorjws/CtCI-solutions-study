# Solution.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def create_minimal_bst(arr: list[int], start: int, end: int) -> TreeNode | None:
    if end < start:
        return None
    mid = (start + end) // 2
    n = TreeNode(arr[mid])
    n.left = create_minimal_bst(arr, start, mid - 1)
    n.right = create_minimal_bst(arr, mid + 1, end)
    return n


# My Solution.
class MyNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class MyTree:
    def __init__(self):
        self.root = None


def get_my_tree(array):
    if len(array) == 1:
        return MyNode(array[0])
    elif len(array) < 1:
        return None
    middle = len(array) // 2
    pivot = array[middle]
    left = array[:middle]
    right = array[middle + 1 :]

    pivot_node = MyNode(pivot)
    pivot_node.left = get_my_tree(left)
    pivot_node.right = get_my_tree(right)

    return pivot_node


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = MyTree()
# t.root = get_my_tree(a)
t.root = create_minimal_bst(a, 0, len(a) - 1)
print(t.root)

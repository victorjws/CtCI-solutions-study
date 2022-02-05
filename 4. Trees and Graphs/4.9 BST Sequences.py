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
def all_sequences(node: Node) -> list[list[int]]:
    result = []
    if node is None:
        result.append([])
        return result

    prefix = [node.value]

    # Recurse on left and right subtrees.
    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)

    # Weave together each list from the left and right sides.
    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result.extend(weaved)
    return result


# Weave lists together in all possible ways.
# This algorithm works by removing the head from one list, recursing, and then
# doing the same thing with the other list.
def weave_lists(
    first: list[int],
    second: list[int],
    results: list[list[int]],
    prefix: list[int],
):
    # One list is empty. Add remainder to [a cloned] prefix and store result.
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    # Recurse with head of first added to the prefix.
    # Removing the head will damage first, so we'll need to put it back where
    # we found it afterwards.
    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)

    # Do the same thing with second, damaging and then restoring the list.
    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)


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
print(all_sequences(node7))

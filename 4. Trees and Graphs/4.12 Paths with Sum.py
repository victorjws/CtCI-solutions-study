# base definition
from collections import deque


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


# Solution 1: Brute Force
def count_paths_with_sum(root: Node, target_sum: int) -> int:
    if root is None:
        return 0

    # Count paths with sum starting from the root.
    paths_from_root = count_paths_with_sum_from_node(root, target_sum, 0)

    # Try the nodes on the left and right
    paths_on_left = count_paths_with_sum(root.left, target_sum)
    paths_on_right = count_paths_with_sum(root.right, target_sum)

    return paths_from_root + paths_on_left + paths_on_right


# Returns the number of paths with this sum starting from this node.
def count_paths_with_sum_from_node(
    node: Node, target_sum: int, current_sum: int
) -> int:
    if node is None:
        return 0

    current_sum += node.value

    total_paths = 0
    if current_sum == target_sum:  # Found a path from the root
        total_paths += 1

    total_paths += count_paths_with_sum_from_node(
        node.left, target_sum, current_sum
    )
    total_paths += count_paths_with_sum_from_node(
        node.right, target_sum, current_sum
    )
    return total_paths


# Solution 2: Optimized
# O(N) time, where N is the number of nodes in the tree.
# In a balanced tree, the space complexity is O(log N) due to the hash table.
# The space complexity can grow to O(N) in an unbalanced tree.
def count_paths_with_sum2(
    node: Node, target_sum: int, running_sum: int = 0, path_count: dict = None
) -> int:
    if path_count is None:
        path_count = dict()
        return count_paths_with_sum2(node, target_sum, running_sum, path_count)

    if node is None:  # base case
        return 0

    # Count paths with sum ending at the current node.
    running_sum += node.value
    sum_ = running_sum - target_sum
    total_paths = path_count.get(sum_, 0)

    # If running_sum equals target_sum, then one additional path starts at root.
    if running_sum == target_sum:
        total_paths += 1

    # Increment path_count, recurse, then decrement path_count.
    increment_hash_table(path_count, running_sum, 1)  # Increment path_count
    total_paths += count_paths_with_sum2(
        node.left, target_sum, running_sum, path_count
    )
    total_paths += count_paths_with_sum2(
        node.right, target_sum, running_sum, path_count
    )
    increment_hash_table(path_count, running_sum, -1)  # Decrement path_count

    return total_paths


def increment_hash_table(hash_table: dict, key: int, delta: int) -> None:
    new_count = hash_table.get(key, 0) + delta
    if new_count == 0:  # Remove when zero to reduce space usage
        hash_table.pop(key, None)
    else:
        hash_table[key] = new_count


# My Solution.
def dfs_sum_nodes(root: Node, target_sum: int) -> int:
    q = [(root, 0)]
    count = 0
    while q:
        node, _sum = q.pop()
        _sum += node.value
        if _sum == target_sum:
            count += 1
        if node.right:
            q.append((node.right, _sum))
        if node.left:
            q.append((node.left, _sum))
    return count


def dfs_start_nodes(root: Node, target_sum: int) -> int:
    q = deque([root])
    total_sum = 0
    while q:
        node = q.popleft()
        total_sum += dfs_sum_nodes(node, target_sum)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return total_sum


node0 = Node(0)
node1 = Node(1)
node2 = Node(1)
node3 = Node(-1)
node4 = Node(0)
node5 = Node(1)
node6 = Node(1)
node7 = Node(1)
node8 = Node(0)
node9 = Node(1)
node10 = Node(-1)
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
print(dfs_start_nodes(node7, 1))
print(count_paths_with_sum(node7, 1))
print(count_paths_with_sum2(node7, 1))

# Solution 1: If linked list size is known
# (length - k)th element.
# Just iterate through the linked list to find this element.


# Solution 2: Recursive. O(n) space.
# Approach A: Don't Return the Element.
from typing import Optional


def print_k_th_to_last(node: "Node", k: int) -> int:
    if node is None:
        return 0
    index: int = print_k_th_to_last(node.next, k) + 1
    if index == k:
        print(f"{k}th to last node is {node.data}")
    return index


# Approach B: Use C++.
# node* nthToLast(node* head, int k, int& i) {
#     if (head == NULL) {
#         return NULL;
#     }
#     node* nd = nthToLast(head->next, k, i);
#     i = i + 1;
#     if (i == k) {
#         return head;
#     }
#     return nd;
# }
#
# node* nthToLast(node* head, int k) {
#     int i = 0;
#     return nthToLast(head, k, i);
# }


# Approach C: Create a Wrapper Class.
class Index:
    value: int = 0


def kth_to_last(head: "Node", k: int, idx: Index = None) -> Optional["Node"]:
    if idx is None:
        idx: Index = Index()
        return kth_to_last(head, k, idx)
    else:
        if head is None:
            return None
        node = kth_to_last(head.next, k, idx)
        idx.value = idx.value + 1
        if idx.value == k:
            return head
        return node


# Solution 3: Iterative. O(n) time and O(1) space.
def nth_to_last3(head: "Node", k: int) -> Optional["Node"]:
    p1 = head
    p2 = head

    for i in range(k):
        if p1 is None:
            return None  # Out of bounds
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


# My Solution
class Node:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


def find(node, index, cur_index: int = 0) -> tuple[int, Optional[str]]:
    if node.next is None:
        total = cur_index
        data = None
    else:
        total, data = find(node.next, index, cur_index + 1)
    if data is None and index == total - cur_index:
        return total, node.data
    return total, data


K = int(input())
input_values = [i for i in input().split()]
prev = h = Node(input_values[0])
for i in input_values[1:]:
    n = Node(i)
    prev.next = n
    prev = n
print(find(h, K))
print(kth_to_last(h, K))

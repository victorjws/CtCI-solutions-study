# Solution. O(N) time.
def delete_dups(n: "Node"):
    hash_set = set()
    previous: Node | None = None
    while n is not None:
        if n.data in hash_set:
            previous.next = n.next
        else:
            hash_set.add(n.data)
            previous = n
        n = n.next


# Follow Up: No Buffer Allowed. O(1) space, O(N^2) time.
def delete_dups_no_buffer(head: "Node"):
    current: Node | None = head
    while current is not None:
        # Remove all future nodes that have the same value
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


# My Solution
class Node:
    def __init__(self, data: int, prev_n: "Node" = None, next_n: "Node" = None):
        self.data = data
        self.prev = prev_n
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


class LinkedList:
    def __init__(self, values: list[int]):
        self.head = Node(values[0])
        before = self.head
        if len(values) <= 1:
            return
        for data in values[1:]:
            node = Node(data, before)
            before.next = node
            before = node

    def __repr__(self):
        node = self.head
        result = ""
        while node is not None:
            result += f"{node.data} "
            node = node.next
        return result

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev


def remove_dups_with_hash_table(linked_list: LinkedList):
    hash_table = {}
    node = linked_list.head
    while node is not None:
        if hash_table.get(node.data) is None:
            hash_table[node.data] = node.data
        else:
            linked_list.remove(node)
        node = node.next


def remove_dups_no_extra_space(linked_list: LinkedList):
    node = linked_list.head
    while node is not None:
        compare_target = node.next
        while compare_target is not None:
            if node.data == compare_target.data:
                linked_list.remove(compare_target)
            compare_target = compare_target.next
        node = node.next


input_values = list(map(int, input().split()))
linked_lst = LinkedList(input_values)
# remove_dups(linked_lst)
# remove_dups_no_extra_space(linked_lst)
delete_dups(linked_lst.head)
# delete_dups_no_buffer(linked_lst.head)
print(linked_lst)

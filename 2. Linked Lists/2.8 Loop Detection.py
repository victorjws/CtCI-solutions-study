# base definition
class Node:
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


# Solution
# use fast runner strategy
def find_beginning(head: Node) -> Node | None:
    slow = head
    fast = head

    # Find meeting point.
    # This will be LOOP_SIZE - k steps into the linked list.
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Collision
            break

    # Error check - no meeting point, and therefore no loop
    if fast is None or fast.next is None:
        return None

    # Move slow to Head. keep fast at Meeting Point. Each are k steps from the
    # Loop Start. If they move at the same pace, they must meet at Loop Start.
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Both now point to the start of the loop.
    return fast


# My Solution
def get_start_of_cycle(node: Node) -> Node | None:
    hash_table = {}
    while node is not None:
        if loop := hash_table.get(id(node)):
            return loop
        hash_table[id(node)] = node.data
        node = node.next
    return None


loop_n = None
prev = head = Node(1)
for i in range(2, 10):
    n = Node(i)
    prev.next = n
    prev = n
    if i == 3:
        loop_n = n
prev.next = loop_n

print(find_beginning(head))
# print(get_start_of_cycle(head))

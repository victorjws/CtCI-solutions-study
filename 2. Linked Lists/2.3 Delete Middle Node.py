# Solution
def delete_node(n: "Node") -> bool:
    if n is None or n.next is None:
        return False
    next: "Node" = n.next
    n.data = next.data
    n.next = next.next
    return True


# My Solution
class Node:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

    def __repr__(self):
        return f"Node ({self.data})"


def remove(node: Node):
    if node.next is not None:
        node.data = node.next.data
        node.next = node.next.next


K = input()
input_values = [i for i in input().split()]
prev = h = Node(input_values[0])
target = None
for i in input_values[1:]:
    n = Node(i)
    prev.next = n
    prev = n
    if n.data == K:
        target = n
remove(target)
n = h
while n is not None:
    print(n.data)
    n = n.next

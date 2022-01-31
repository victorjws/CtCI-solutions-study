# Solution.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __len__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return len(nodes)

    def add_last(self, n):
        node = Node(n)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def poll(self):
        value = self.head
        self.head = value.next
        return value.data

    def peek(self):
        return self.head.data


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.order = None

    def set_order(self, order: int):
        self.order = order

    def get_order(self):
        return self.order

    # Compare orders of animals to return the older item.
    def is_older_than(self, a: "Animal"):
        return self.order < a.get_order()

    def __gt__(self, other):  # pythonic version of is_order_than()
        return self.order > other.order

    def __repr__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def __init__(self, n):
        super().__init__(n)

    def __repr__(self):
        return f"Dog({self.name})"


class Cat(Animal):
    def __init__(self, n):
        super().__init__(n)

    def __repr__(self):
        return f"Cat({self.name})"


class AnimalQueue:
    def __init__(self):
        self.order = 0  # acts as timestamp
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def __repr__(self):
        return f"AnimalQueue(dogs)(cats )"

    def enqueue(self, a: Animal):
        # Order is used as sort of timestamp, so that we can compare the
        # insertion order of a dog to a cat.
        a.set_order(self.order)
        self.order += 1

        if isinstance(a, Dog):
            self.dogs.add_last(a)
        elif isinstance(a, Cat):
            self.cats.add_last(a)

    def dequeue_any(self) -> Animal:
        # Look at tops of dog and cat queues, and pop the queue with the oldest
        # value.
        if len(self.dogs) == 0:
            return self.dequeue_cats()
        elif len(self.cats) == 0:
            return self.dequeue_dogs()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.is_older_than(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self):
        return self.dogs.poll()

    def dequeue_cats(self):
        return self.cats.poll()


# My Solution.
class MyAnimal:
    def __init__(self, type_: str, arrival_time, next_=None):
        self.type = type_
        self.arrival_time = arrival_time
        self.next = next_

    def __repr__(self):
        return f"Animal({self.type} {self.arrival_time})"


class MyAnimalQueue:
    def __init__(self, types: list[str], times: list[int]):
        self.dog_head = None
        self.dog_tail = None
        self.cat_head = None
        self.cat_tail = None

        cat_node = None
        dog_node = None
        for i, t in enumerate(types):
            animal = MyAnimal(t, times[i])
            if animal.type == "cat":
                if cat_node is None:
                    cat_node = animal
                    self.cat_head = cat_node
                    self.cat_tail = cat_node
                else:
                    cat_node.next = animal
                    self.cat_tail = animal
                    cat_node = animal
            else:
                if dog_node is None:
                    dog_node = animal
                    self.dog_head = dog_node
                    self.dog_tail = dog_node
                else:
                    dog_node.next = animal
                    self.dog_tail = animal
                    dog_node = animal

    def __repr__(self):
        return f"AnimalQueue (cat {self.cat_head} {self.cat_tail} dog {self.dog_head} {self.dog_tail})"

    def enqueue(self, value):
        if value.type == "cat":
            self.cat_tail.next = value
            self.cat_tail = value
        else:
            self.dog_tail.next = value
            self.dog_tail = value

    def dequeue_any(self):
        if self.dog_head.arrival_time >= self.cat_head.arrival_time:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()

    def dequeue_dog(self):
        value = self.dog_head
        self.dog_head = self.dog_head.next
        return value

    def dequeue_cat(self):
        value = self.cat_head
        self.cat_head = self.cat_head.next
        return value


# types = ["cat", "dog", "dog", "cat", "dog", "cat"]
# arrival_time = [1, 2, 3, 4, 5, 6]
# q = MyAnimalQueue(types, arrival_time)
# print(q.dequeue_any())
# print(q.dequeue_dog())
# print(q.dequeue_any())
# print(q.dequeue_cat())

animals = [Cat("a"), Dog("b"), Cat("c"), Cat("d"), Dog("e"), Dog("f")]
q = AnimalQueue()
for animal in animals:
    q.enqueue(animal)
print(q.cats)
print(q.dogs)
print(q.dequeue_any())
print(q.dequeue_dogs())
print(q.dequeue_any())
print(q.dequeue_cats())

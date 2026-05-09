from collections import deque

# ---------------- STACK ----------------
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)


# ---------------- QUEUE ----------------
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)


# ---------------- LINKED LIST ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        print("Linked List:", elements)


# ---------------- TESTING ----------------

# Stack Testing
print("----- STACK -----")
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack Size:", stack.size())
print("Top Element:", stack.peek())
print("Popped Element:", stack.pop())
print("Stack Size After Pop:", stack.size())

# Queue Testing
print("\n----- QUEUE -----")
queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Queue Size:", queue.size())
print("Dequeued Element:", queue.dequeue())
print("Queue Size After Dequeue:", queue.size())

# Linked List Testing
print("\n----- LINKED LIST -----")
linked_list = LinkedList()

linked_list.append(100)
linked_list.append(200)
linked_list.append(300)

linked_list.display()

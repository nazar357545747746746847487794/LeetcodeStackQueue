class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        val = self.top.val
        self.top = self.top.next
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.top.val

    def is_empty(self):
        return self.top is None



class MyQueue:

    def __init__(self):
        self.s_in = Stack()
        self.s_out = Stack()

    def push(self, x):
        self.s_in.push(x)

    def pop(self):
        self.peek()
        return self.s_out.pop()

    def peek(self):
        if self.s_out.is_empty():
            while not self.s_in.is_empty():
                self.s_out.push(self.s_in.pop())
        return self.s_out.peek()

    def empty(self):
        return self.s_in.is_empty() and self.s_out.is_empty()

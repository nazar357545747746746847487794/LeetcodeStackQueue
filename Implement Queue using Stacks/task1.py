class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class MyQueue:

    def __init__(self):
        self.s_in = Stack()
        self.s_out = Stack()


    def push(self, x: int) -> None:
        self.s_in.push(x)



    def pop(self) -> int:
        self.peek()
        return self.s_out.pop()




    def peek(self) -> int:
        if self.s_out.is_empty():
            while not self.s_in.is_empty():
                item = self.s_in.pop()
                self.s_out.push(item)
        return self.s_out.peek()



    def empty(self) -> bool:
        return self.s_in.is_empty() and self.s_out.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

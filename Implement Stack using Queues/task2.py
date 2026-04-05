class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x: int) -> None:
        self.items.append(x)

    def dequeue(self) -> int:
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self) -> int:
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        return self.q1.dequeue()


    def top(self) :
        return self.q1.peek()


    def empty(self):
        return self.q1.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

from collections import deque


class FreqStack:

    def __init__(self):
        self.freq = deque()
        self.group = deque()
        self.max_freq = 0

    def push(self, val):
        f = 0
        for item in self.freq:
            if item[0] == val:
                item[1] += 1
                f = item[1]
                break
        else:
            f = 1
            self.freq.append([val, 1])

        for item in self.group:
            if item[0] == f:
                item[1].append(val)
                break
        else:
            self.group.append([f, deque([val])])

        if f > self.max_freq:
            self.max_freq = f

    def pop(self):
        for item in self.group:
            if item[0] == self.max_freq:
                val = item[1].pop()
                if not item[1]:
                    self.max_freq -= 1
                for entry in self.freq:
                    if entry[0] == val:
                        entry[1] -= 1
                        break
                return val

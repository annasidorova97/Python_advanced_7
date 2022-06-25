class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Stack after pushes:", s.display())
print("Pop:", s.pop())
print("Stack after pop:", s.display())

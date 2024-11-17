# Question 1: Write a Python program to implement a stack.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# Demonstration of Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.display()
print("Popped:", stack.pop())
stack.display()

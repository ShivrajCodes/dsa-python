# Question 2: Write a Python program to implement a queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


# Demonstration of Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.display()
print("Dequeued:", queue.dequeue())
queue.display()
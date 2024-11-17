# Question 4: Write a Python program to implement a circular queue using an array.
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued {item}")
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Demonstration of Circular Queue
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()
cq.dequeue()
cq.dequeue()
cq.enqueue(60)
cq.display()






class Array:
    def __init__(self, size):
        self.A = [0] * size
        self.size = size
        self.length = 0

    def display(self):
        for i in range(self.length):
            print(self.A[i], end=" ")
        print()

    def append(self, x):
        if self.length < self.size:
            self.A[self.length] = x
            self.length += 1

    def insert(self, index, x):
        for i in range(self.length, index, -1):
            self.A[i] = self.A[i - 1]
        self.A[index] = x
        self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            return -1
        x = self.A[index]
        for i in range(index, self.length - 1):
            self.A[i] = self.A[i + 1]
        self.length -= 1
        return x

arr_size = int(input("Enter size of array: "))
arr = Array(arr_size)
n = int(input("Enter number of elements in array: "))
print("Enter the elements in the array:")
for i in range(n):
    arr.A[i] = int(input())
arr.length = n
arr.display()

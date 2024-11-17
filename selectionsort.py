def swap(x, y):
    return y, x

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = swap(arr[i], arr[k])

def main():
    A = [11, 13, 7, 22, 16, 9]
    selection_sort(A)
    for num in A:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()

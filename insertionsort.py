def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
      j=i-1
      x=arr[i]
      while j>=0 and arr[i]>x:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=x
def main():
    A=[11,13,10,7,15,12]
    n=len(A)
    insertion_sort(A)
    for num in A:
        print(num, end="")
    print()
if __name__=="__main__":
    main()

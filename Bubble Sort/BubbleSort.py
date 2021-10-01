def bubbleSort(arr, n):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

n = int(input())
arr = list(map(int, input().strip().split()))
print(bubbleSort(arr, n))

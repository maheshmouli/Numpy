def bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
        if swapped == False:
            break

arr = [3,9,2,1,5,4,7,8]
bubble_Sort(arr)
print("Sorted Array:")
for i in range(len(arr)):
    print("%d "%arr[i], end=" ")
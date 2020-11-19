def binary(arr, start, end, x):
    if end >= start:
        mid = start + (end - start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binary(arr, start, mid-1, x)
        else:
            return binary(arr, mid+1, end, x)  
    return -1

arr =sorted([2,5,1,3,7,8,4,0])
x = 5
result = binary(arr, 0, len(arr)-1, x)
if result != -1:
    print(arr)
    print("Element found at "+ str(result))
else:
    print("Element not found")
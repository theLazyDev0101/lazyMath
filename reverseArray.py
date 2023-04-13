def reverseArr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7]
print(arr)
reverseArr(arr,0,6)
print(arr)
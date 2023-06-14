def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr1=[1,5,4,8,4,9,26,5,4,5]
bubblesort(arr1)
print(arr1)
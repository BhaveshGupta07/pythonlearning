def insertion_sort(array):
    for i in range(1,len(array)) :
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1] = key

arr1=[1,5,4,8,4,9,26,5,4,5]
insertion_sort(arr1)
print(arr1)
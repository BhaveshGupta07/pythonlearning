def selection_sort(array):
    for i in range(len(array)):
        min_ind=i
        for j in range(i+1,len(array)):
            if array[min_ind]>array[j]:
                min_ind=j
        (array[i],array[min_ind])=(array[min_ind],array[i])

arr1=[1,5,4,8,4,9,26,5,4,5]
selection_sort(arr1)
print(arr1)
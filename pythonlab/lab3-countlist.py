def count_elements(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_elements(item)
        else:
            count += 1
    return count

#the above function is just iterating over itself and check if the list contains elements or list

my_list = ['d', ['a', 'b', 'c'], 1, 2, [5, 6, [8, 9]], 3, 5, 48, 98,5,[56,5,4,8]]
num_elements = count_elements(my_list)
print(f"The number of elements in the list is: {num_elements}")
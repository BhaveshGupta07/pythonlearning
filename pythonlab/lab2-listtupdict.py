def print_elements(list_data, dict_data, tuple_data, set_data):
    print("Elements of the List:")
    for element in list_data:
        print(element)

    print("\nElements of the Dictionary:")
    for key, value in dict_data.items():
        print(f"{key}: {value}")

    print("\nElements of the Tuple:")
    for element in tuple_data:
        print(element)

    print("\nElements of the Set:")
    for element in set_data:
        print(element)


lis=input("enter the list data ").split()
list_data=list(int(element) for element in lis)
dict_data={}
lenth=int(input("enter the length of the dictiornary data"))
for i in range(lenth):
    alpha = input("Enter alphabets: ")
    num = input("Enter the num: ")

    dict_data[alpha] = num 

tup=input("enter the tupple data ").split()
tupple_data=tuple(int(element) for element in tup)
sets=input("enter the set data ").split()
set_data=set(int(element) for element in sets)

print_elements(list_data,dict_data,tupple_data,set_data)
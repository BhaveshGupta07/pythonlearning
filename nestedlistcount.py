list= [[12,54,5,7,8],[12,56,4,7,5,8],[56,55,68,45,5,4],[5,8,4,7,5,8,8,7,5]]
def getnumber(list):
    count = 0
    for element in list:
        count += len(element)
    return count

print("total number of elements in a list: %d" % len(list),getnumber(list))
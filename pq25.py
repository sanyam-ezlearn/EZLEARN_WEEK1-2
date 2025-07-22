'''Merge Two Sorted Lists'''
def merge2Lists(i, j):
    mergedlist = []
    while (i and j):
        if (i[0] <= j[0]):
            item = i.pop(0)
            mergedlist.append(item)
        else:
            item = j.pop(0)
            mergedlist.append(item)
    mergedlist.extend(i if i else j)
    return mergedlist

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

print(merge2Lists(list1, list2))
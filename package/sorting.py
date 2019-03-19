def bubble_sort(items):
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items
    '''Return array of items, sorted in ascending order'''

def merge_sort(items):
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items
'''Return array of items, sorted in ascending order'''
def quick_sort(items):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else :
                greater.append(i)

        return quick_sort(less)+quick_sort(equal)+quick_sort(greater)

    else:
        return array

'''Return array of items, sorted in ascending order'''        

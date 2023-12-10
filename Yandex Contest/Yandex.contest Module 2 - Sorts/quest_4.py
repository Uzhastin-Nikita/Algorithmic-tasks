def Sort(array, numbers):
    List = [0]*numbers
    return merge_sort(array, List, 0, numbers-1)

def merge_sort(array, List, left, right):
    count_ = 0
    if left < right:
        middle = (left + right)//2
        count_ += merge_sort(array, List, left, middle)
        count_ += merge_sort(array, List, middle + 1, right)
        count_ += Merge(array, List, left, middle, right)
    return count_

def Merge(array, List, left, middle, right):
    i = left     
    j = middle + 1 
    k = left     
    count_ = 0
    while i <= middle and j <= right:
        if array[i] <= array[j]:
            List[k] = array[i]
            k += 1
            i += 1
        else:
            List[k] = array[j]
            count_ += (middle-i + 1)
            k += 1
            j += 1
    while i <= middle:
        List[k] = array[i]
        k += 1
        i += 1
    while j <= right:
        List[k] = array[j]
        k += 1
        j += 1
    for item in range(left, right + 1):
        array[item] = List[item]    
    return count_

leght = int(input())
array = list(map(int, input().split())) 
numbers = len(array)
array = Sort(array, numbers)
print(array) 

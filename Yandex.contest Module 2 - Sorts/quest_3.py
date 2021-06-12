def merge(left_list, right_list, start_index, end_index):
    sort_list = []
    left_list_index = right_list_index = 0

    left_list_lenght, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_lenght + right_list_length):
        if left_list_index < left_list_lenght and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sort_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sort_list.append(right_list[right_list_index])
                right_list_index += 1
        
    sort_list += left_list[left_list_index:]
    sort_list += right_list[right_list_index:]

    print(start_index + 1, end_index + 1, sort_list[0], sort_list[-1])
        
    return sort_list

def merge_sort(numbers, start_index, end_index):
    if len(numbers) <= 1:
        return numbers
    
    middle = len(numbers) // 2

    left_list = merge_sort(numbers[:middle], start_index, start_index + middle -1)
    right_list = merge_sort(numbers[middle:], start_index + middle, end_index)

    sort = merge(left_list, right_list, start_index, end_index) 

    return sort

lenght = int(input())

nums = list(map(int, input().split()))
res = merge_sort(nums, 0, lenght - 1)
print(' '.join(map(str, res)))
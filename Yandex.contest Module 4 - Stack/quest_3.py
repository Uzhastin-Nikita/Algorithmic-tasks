length = int(input())
array = list(zip(list(map(int, input().split())), range(length)))

stack = []
result = [0]*length

for item in array[::-1]:
    while (stack != []) and (stack[-1][0] >= item[0]):
        stack.pop()
    if stack == []:
        result[item[1]] = -1
    else:
        result[item[1]] = stack[-1][1]
    stack.append(item)
    
print(' '.join(map(str, result)))
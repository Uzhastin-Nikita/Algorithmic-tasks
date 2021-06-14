def minimal_search(array, n, k):
    stack = []

    for item in range(k):
        while (stack != []) and (array[item] <= array[stack[-1]]):
            stack.pop()

        stack.append(item)
    for item in range(k, n):
        print(array[stack[0]])
        while (stack != []) and (item-k >= stack[0]):
            stack.pop(0)

        while (stack != []) and (array[item] <= array[stack[-1]]):
            stack.pop()

        stack.append(item)
    print(array[stack[0]])

n, k = map(int, input().split())
array = list(map(int, input().split()))
minimal_search(array, n, k)
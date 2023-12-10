num = int(input())

first_train = list(map(int,input().split()))
second_train = []

stack = []  # тупик

complete_train =  sorted(first_train)

for item in range(num):
    if (stack == []) or (stack[-1] > first_train[0]):
        stack.append(first_train[0])
        first_train.pop(0)
    else:
        while (stack != [] and stack[-1] < first_train[0]):
            second_train.append(stack[-1])
            stack.pop(-1)
        if (stack == []) or (stack[-1] > first_train[0]):
            stack.append(first_train[0])
            first_train.pop(0)        

if stack != []: 
    for item in range(len(stack)):
        second_train.append(stack[-1])
        stack.pop(-1)   

if second_train == complete_train:
    print("YES")
else: 
    print("NO") 

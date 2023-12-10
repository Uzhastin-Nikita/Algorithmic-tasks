def function(string):
    count = 0

    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        elif (stack != []) and (stack[-1] == '('):
            stack.pop()
        else:
            count += 1
    
    return count + len(stack)

string = input()

print(function(string))
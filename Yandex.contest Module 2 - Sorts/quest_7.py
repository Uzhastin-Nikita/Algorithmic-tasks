array = []
size = int(input())

for item in range(size):
    array.append(input())

print('Initial array:')
print(', '.join(array))

count = len(array[0])
Phase = 0
for item in range(reversed(count)):
    Phase += 1
    print('**********')
    print(f'Phase {Phase}')
    bucket = [[] for _ in range(10)]
    for j in range(len(array)):
        bucket[ord(array[0][item]) - ord('0')].append(array[j])
    for j in range(10):
        if len(bucket[j]) == 0:
            print(f'Bucket {j}: empty')
        else:
            print('Bucket ' + str(j)+": ", end='')
            for now in range(len(bucket[j])-1):
                print(bucket[j][now], end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(10):
        for k in range(len(bucket[j])):
            array[p] = bucket[j][k]
            p += 1

print('**********')
print('Sorted array:')

print(', '.join(array))
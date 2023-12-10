n = int(input())
res = []
for i in range(n):
    number, value = map(int, input().split())
    res.append([number, value])
for i in range(n-1):
    for j in range(n-i-1):
        if res[j][1] < res[j+1][1]:
            res[j], res[j+1] = res[j+1], res[j]
        if res[j][1] == res[j+1][1]:
            if res[j][0] > res[j+1][0]:
                res[j], res[j+1] = res[j+1], res[j]
print()
[print(i[0], i[1]) for i in res] 
            

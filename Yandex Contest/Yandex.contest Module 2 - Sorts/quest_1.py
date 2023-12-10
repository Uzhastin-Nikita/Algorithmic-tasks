n = input()
array = input()

str_list = array.split(" ")
res = []

for item in str_list:
    res.append(int(item))

n = len(res)
num_swap = 0

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if res[j] > res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]
            num_swap+=1
            print(" ".join(map(str, res)))
if num_swap == 0:
    print('num_swap = 0')
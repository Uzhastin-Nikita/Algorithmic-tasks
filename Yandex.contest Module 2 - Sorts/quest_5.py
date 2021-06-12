n = int(input())
array = input()

str_list = array.split(" ")
res = []

for item in str_list:
    res.append(int(item))

print(len(set(res).intersection(set(res))))

products_quan = int(input())
products = list(map(int, input().split()))

order_Quan = int(input())
order = list(map(int, input().split()))

count = [0] * (products_quan + 1)
for item in order:
    count[item] += 1

for i in range(products_quan):
    if products[i] < count[i+1]:
        print('yes')
    else:
        print('no')
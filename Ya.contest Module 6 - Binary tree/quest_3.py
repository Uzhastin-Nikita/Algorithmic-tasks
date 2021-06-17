# RMQ - _ _ _ _ _ деревья отрезков.
# RSQ - запрос диапозона суммы.
# 4 * n - место, выделяемое для отрезка

from math import gcd # модуль для вычисления наибольшего общего делителя

def build(v, left, right, segment_tree, value):
    if right - left == 1:
        segment_tree[v] = value[left]
        return
    middle = (right + left) // 2

    build(2*v+1, left, middle, segment_tree, value)
    build(2*v+2, middle, right, segment_tree, value)
    
    segment_tree[v] = gcd(value[2*v+1], value[2*v+2])

def get_gcd(v, left, right, segment_tree, q_left, q_right):
    if q_left <= left and q_right >= right:
        return segment_tree[v]
    if q_left >= r or q_right <= left:
        return 0
    middle = (right + left) // 2
    t_left = get_gcd(2*v+1, left, middle, segment_tree, q_left, q_right)
    t_right = get_gcd(2*v+2, middle, right, segment_tree, q_left, q_right)
    return gcd(t_left, t_right)

numbers = int(input())
res = list(map(int, input().split()))
segment_tree = [0]*4*numbers
build(0, 0, numbers, segment_tree, res)
q = int(input())
index = []
while q != 0:
    left, right = map(int, input())
    index.append(get_gcd(0, 0, numbers, segment_tree, left-1, right))
    q -= 1

print(*index)
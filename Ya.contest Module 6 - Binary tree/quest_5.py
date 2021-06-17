from math import gcd

def build(value, left, right, segm_tree, num):
    if right - left == 1:
        segm_tree[value] = num[left]
        return

    middle = (right + left) // 2

    build(2*value + 1, left, middle, segm_tree, num)
    build(2*value + 2, middle, right, segm_tree, num)

    segm_tree[value] = gcd(segm_tree[2*value + 1], segm_tree[2*value + 2])


def update(value, left, right, segm_tree, index, nums):
    if right - left == 1:
        segm_tree[value] = nums
        return

    middle = (left + right) // 2

    if index < middle:
        update(2*value + 1, left, middle, segm_tree, index, nums)
    else:
        update(2*value + 2, middle, right, segm_tree, index, nums)

    segm_tree[value] = gcd(segm_tree[2*value + 1], segm_tree[2*value + 2])


def get_NOD(value, left, right, segm_tree, q_left, q_right):
    if q_left <= left and q_right >= right:
        return segm_tree[value]
    if q_left >= right or q_right <= left:
        return 0

    middle = (right + left) // 2

    st_left = get_NOD(2*value + 1, left, middle, segm_tree, q_left, q_right)
    st_right = get_NOD(2 * value + 2, middle, right, segm_tree, q_left, q_right)

    return gcd(st_left, st_right)

n = int(input())
numbers = list(map(int, input().split()))[:n]

segment_tree = [0 ] * 4 * n

build(0, 0, n, segment_tree, numbers)
q = int(input())
result = []

while q != 0:
    type, left, right = map(str, input().split())

    if type == 's':
        result.append(get_NOD(0, 0, n, segment_tree, int(left) - 1, int(right)))
    else:
        update(0, 0, n, segment_tree, int(left) - 1, int(right))

    q -= 1

print(*result)
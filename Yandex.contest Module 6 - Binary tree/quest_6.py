def build(value, left, right, segments_tree, numbers):
    if right - left == 1:
        segments_tree[value] = numbers[left]
        return

    middle = (right + left) // 2

    build(2 * value + 1, left, middle, segments_tree, numbers)
    build(2 * value + 2, middle, right, segments_tree, numbers)

    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

# search k-zero
def get_k_zero(value, left, right, segments_tree, number):
    if number > segments_tree[value]:
        return -1
    if right - left == 1:
        return right

    middle = (right + left) // 2

    if segments_tree[2 * value + 1] >= number:
        return get_k_zero(2 * value + 1, left, middle, segments_tree, number)
    else:
        return get_k_zero(2 * value + 2, middle, right, segments_tree, number - segments_tree[2 * value + 1])

def get_sum(value, left, right, segments_tree, q_left, q_right):
    if q_left <= left and q_right >= right:
        return segments_tree[value]

    if q_left >= right or q_right <= left:
        return 0

    middle = (right + left) // 2

    t_left = get_sum(2 * value + 1, left, middle, segments_tree, q_left, q_right)
    t_right = get_sum(2 * value + 2, middle, right, segments_tree, q_left, q_right)

    return t_left + t_right

# just add update-function for dinamic-tree
def update(value, left, right, segments_tree, index, number):
    if right - left == 1:
        segments_tree[value] = number
        return

    middle = (right + left) // 2
    if index < middle:
        update(2 * value + 1, left, middle, segments_tree, index, number)
    else:
        update(2 * value + 2, middle, right, segments_tree, index, number)
    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

n = int(input())
# craft list for next work
numbers = [0 if int(i) != 0 else 1 for i in input().split()] 

segments_tree = [0] * 4 * n
build(0, 0, n, segments_tree, numbers)
q = int(input())

res = []
while q != 0:
    # add item
    item = input().split()
    # check on 4, this is for beauty, we break it into threes and fours
    if len(item) == 4:
        # input data
        left, right, number = int(item[1]), int(item[2]), int(item[3])
        # get our sum
        sum = get_sum(0, 0, n, segments_tree, left-1, right)
        # if sum > number and left > 1 -> add in res k_zero + our sum
        if sum >= number and left > 1:
            res.append(get_k_zero(0, 0, n, segments_tree, number + get_sum(0, 0, n, segments_tree, 0, left - 1)))
        # if sum > number and left == 1 -> add in res k_zero
        elif sum >= number and left == 1:
            res.append(get_k_zero(0, 0, n, segments_tree, number))
        # else add -1
        else:
            res.append(-1)
    else:
        first, second = int(item[1]), int(item[2])
        # if second_data == 0 -> update() - number = 0
        if second == 0:
            update(0, 0, n, segments_tree, first-1, 1)
        # else -> update() - number = 1
        else:
            update(0, 0, n, segments_tree, first-1, 0)
    q -= 1

print(*res)


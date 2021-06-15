class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right)) + 1


def build_tree(elements):
    root = Node(elements[0])
    for item in range(1, len(elements)):
        root.add(elements[item])
    return root


def check_balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and check_balance(tree.right) and check_balance(tree.left)):
        return True
    return False


numbers = [int(item) for item in input().split()]
numbers.pop()

tree = build_tree(numbers)

if check_balance(tree):
    print("YES")
else:
    print("NO")
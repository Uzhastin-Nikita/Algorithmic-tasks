class Node:
    __size = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1
    
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if not self.left and not self.right:
            print(self.data)
        if self.right:
            self.right.find_fork()
    
    def add(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if (self.left and self.right is None) or (self.left is None and self.right):
            print(self.data)
        if self.right:
            self.right.find_fork()
        
def build_tree(elements):
    root = Node(elements[0])
    for item in range(1, len(elements)):
        root.add(elements[item])
    return root

numbers = [int(item) for item in input().split()]
numbers.pop()

tree = build_tree(numbers)

tree.find_fork()
    
class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = 4
root.left = Tree()
root.left.data = 2
root.right = Tree()
root.right.data = 7

root.left.left = Tree()
root.left.left.data = 1
root.left.right = Tree()
root.left.right.data = 3

root.right.left = Tree()
root.right.left.data = 6
root.right.right = Tree()
root.right.right.data = 9


def invertTree(root):
    if root == None:
        return None

    root.left , root.right = root.right , root.left
    invertTree(root.left)
    invertTree(root.right)

def preorcer(root):
    if root == None:
        return None
    print(root.data)
    preorcer(root.left)
    preorcer(root.right)



print("before")
preorcer(root)
print("after")
invertTree(root)
preorcer(root)
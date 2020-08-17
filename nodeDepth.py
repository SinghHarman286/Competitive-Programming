
class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):

    sum = 0

    return nodeDepthsHelper(root, sum)

def nodeDepthsHelper(root, sum):

    sum = root.value

    if root.left:
        sum += nodeDepthsHelper(root.left, sum)
    if root.right:
        sum += nodeDepthsHelper(root.right, sum)

    return sum

root = BT(1)
root.left = BT(2)
root.right = BT(3)
root.left.left = BT(4)
root.left.right = BT(5)
root.right.left = BT(6)
root.right.right = BT(7)
root.left.left.left = BT(8)
root.left.left.right = BT(9)
root.left.right.left = BT(10)

print(nodeDepths(root))
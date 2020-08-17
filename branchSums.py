# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    arr = []
    sum = 0

    def transverse(node, sum):
        sum += node.value
        print(node.value, sum)
        if node.left:
            transverse(node.left, sum)
        arr.append(sum)
        if node.right:
            transverse(node.right, sum)
            
    transverse(root, sum)

    return arr

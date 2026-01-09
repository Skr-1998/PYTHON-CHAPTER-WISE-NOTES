# Node class for BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to convert sorted array to Balanced BST
def sortedArrayToBST(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr, start, mid - 1)
    root.right = sortedArrayToBST(arr, mid + 1, end)

    return root


# Preorder Traversal (Root -> Left -> Right)
def preOrder(node):
    if node is None:
        return

    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)

root = sortedArrayToBST(arr, 0, n - 1)

print("Preorder traversal of the Balanced BST:")
preOrder(root)

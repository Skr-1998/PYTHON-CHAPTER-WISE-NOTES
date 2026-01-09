class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return []

    q = [root]
    res = []
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])
        
        for i in range(len_q):
            node = q.pop(0)  # Popping from front of the queue
            res[curr_level].append(node.data)

            # left child
            if node.left is not None:
                q.append(node.left)
            
            # right child
            if node.right is not None:
                q.append(node.right)
        
        curr_level += 1
    
    return res

# Create tree nodes
root = Node(5)
root.left = Node(12)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(14)

# Perform level order traversal (BFS)
res = levelOrder(root)

# Print results
for level in res:
    for val in level:
        print(val, end=' ')
    print()

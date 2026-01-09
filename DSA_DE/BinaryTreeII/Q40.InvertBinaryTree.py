def InvertedTree(self,root):
    if root is None:
        return
    left_subtree = self.InvertedTree(root.left)
    right_subtree = self.InvertedTree(root.right)

    root.left = right_subtree
    root.right = left_subtree

    return root
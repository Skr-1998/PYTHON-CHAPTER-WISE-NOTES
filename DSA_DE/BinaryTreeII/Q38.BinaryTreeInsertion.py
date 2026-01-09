def Insertion(root,x):
    if root is None:
        return Tree(x)
    
    if root.data > x:
        root.left = Insertion(root.left,x)
    else:
         root.right = Insertion(root.right,x)   
    return root         

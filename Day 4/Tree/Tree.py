class Node:
    def __init__(self, data):
        self.data = data          # Data stored in the node
        self.left = None          # Left child
        self.right = None         # Right child

# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=' ')   # Visit root
        preorder(root.left)         # Traverse left subtree
        preorder(root.right)        # Traverse right subtree

# Inorder Traversal: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)          # Traverse left subtree
        print(root.data, end=' ')   # Visit root
        inorder(root.right)         # Traverse right subtree

# Postorder Traversal: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)        # Traverse left subtree
        postorder(root.right)       # Traverse right subtree
        print(root.data, end=' ')   # Visit root


# Creating nodes
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

print("Preorder Traversal:")
preorder(root)     # Output: A B D E C F

print("\nInorder Traversal:")
inorder(root)      # Output: D B E A C F

print("\nPostorder Traversal:")
postorder(root)    # Output: D E B F C A
print("\n")
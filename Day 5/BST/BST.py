"""
Binary Search Tree (BST)

A Binary Search Tree is a node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees.

This data structure allows for efficient searching, insertion, and deletion of elements.

Describes the functionality and usage of the provided Binary Search Tree implementation, including methods for inserting, searching, and traversing nodes.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)
        print(f"Inserted {key} into BST.")
    
    def _insert_rec(self, node, key):
        """Helper method to insert a new key recursively."""
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)
        # If the key is equal, do nothing (no duplicates allowed)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search_rec(self.root, key)
    
    def _search_rec(self, node, key):
        """Helper method to search for a key recursively."""
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)
    
    def inorder_traversal(self):
        """Perform an inorder traversal of the BST."""
        print("Inorder Traversal:")
        self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_rec(node.left)
            print(node.val, end=' ')
            self._inorder_rec(node.right)

    def preorder_traversal(self):
        """Perform a preorder traversal of the BST."""
        print("Preorder Traversal:")
        self._preorder_rec(self.root)

    def _preorder_rec(self, node):
        """Helper method for preorder traversal."""
        if node:
            print(node.val, end=' ')
            self._preorder_rec(node.left)
            self._preorder_rec(node.right)
            
    def postorder_traversal(self):
        """Perform a postorder traversal of the BST."""
        print("Postorder Traversal:")
        self._postorder_rec(self.root)

    def _postorder_rec(self, node):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_rec(node.left)
            self._postorder_rec(node.right)
            print(node.val, end=' ')

    def find_min(self):
        """Find the minimum value in the BST."""
        if self.root is None:
            return None
        return self._find_min_rec(self.root)
    
    def _find_min_rec(self, node):
        """Helper method to find the minimum value recursively."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        """Find the maximum value in the BST."""
        if self.root is None:
            return None
        return self._find_max_rec(self.root)
    
    def _find_max_rec(self, node):
        """Helper method to find the maximum value recursively."""
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete_rec(self.root, key)
        print(f"Deleted {key} from BST.")

    def _delete_rec(self, node, key):  
        """Helper method to delete a key recursively."""
        if node is None:
            return node
        
        if key < node.val:
            node.left = self._delete_rec(node.left, key)
        elif key > node.val:
            node.right = self._delete_rec(node.right, key)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._find_min_rec(node.right)
            node.val = successor.val
            node.right = self._delete_rec(node.right, successor.val)
        
        return node
    
    def is_empty(self):
        """Check if the BST is empty."""
        return self.root is None
    
    def height(self):
        """Calculate the height of the BST."""
        return self._height_rec(self.root)
    def _height_rec(self, node):
        """Helper method to calculate the height recursively."""
        if node is None:
            return -1
        left_height = self._height_rec(node.left)
        right_height = self._height_rec(node.right) 
        return 1 + max(left_height, right_height)
    def clear(self):    
        """Clear the BST."""
        self.root = None    

    def __str__(self):
        """String representation of the BST."""
        return f"BST with root value: {self.root.val if self.root else 'None'}"
    def __repr__(self):
        """Representation of the BST."""
        return f"BST({self.root})"
    
# Example usage:    

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

if bst.search(7):
    print("Found:", bst.search(7).val)  # Should print: Found: 7
else:
    print("Not found") 
    
bst.inorder_traversal()  # Should print: 3 5 7 10 15
print()

bst.preorder_traversal()  # Should print: 10 5 3 7 15
print()

bst.postorder_traversal()  # Should print: 3 7 5 15 10
print()

print("Minimum value:", bst.find_min().val)  # Should print: Minimum value: 3
print("Maximum value:", bst.find_max().val)  # Should print: Maximum value: 15

bst.delete(5)
bst.inorder_traversal()  # Should print: 3 7 10 15
print()

print("Height of BST:", bst.height())  # Should print the height of the BST
    
    
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
    # key: The value to be stored in the node

    def __init__(self, key):
        """Initialize a new node with the given key."""
        self.left = None                # left: Reference to the left child node (initially None)
        self.right = None               # right: Reference to the right child node (initially None)
        self.val = key                  # val: The value stored in the node, set to the provided key

class BST:
    def __init__(self):
        self.root = None                # root: The root node of the BST, initially set to None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:           
            self.root = Node(key)       # If the tree is empty, create a new root node
        else:
            self._insert_rec(self.root, key)    # Otherwise, insert the key recursively
        print(f"Inserted {key} into BST.")
    
    def _insert_rec(self, node, key):
        """Helper method to insert a new key recursively."""
        if key < node.val:                      # If the key is less than the current node's value
            # Insert the key in the left subtree 
            if node.left is None:
                node.left = Node(key)           # Insert as left child if left is empty
            else:
                self._insert_rec(node.left, key) # Recur on left subtree
        elif key > node.val:                    # If the key is greater than the current node's value   
            # Insert the key in the right subtree
            if node.right is None:
                node.right = Node(key)          # Insert as right child if right is empty
            else:
                self._insert_rec(node.right, key) # Recur on right subtree
        # If the key is equal, do nothing (no duplicates allowed)

    def search(self, key):                      
        """Search for a key in the BST."""
        return self._search_rec(self.root, key)     
    
    def _search_rec(self, node, key):
        """Helper method to search for a key recursively."""
        if node is None or node.val == key:             
            # If node is None (key not found) or node's value matches the key, return node
            return node
        if key < node.val:
            return self._search_rec(node.left, key)     # If key is less than current node's value, search in left subtree
        return self._search_rec(node.right, key)        # If key is greater than current node's value, search in right subtree
    
    def inorder_traversal(self):
        """Perform an inorder traversal of the BST."""
        print("Inorder Traversal:")
        self._inorder_rec(self.root)                    

    def _inorder_rec(self, node):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_rec(node.left)                # Traverse left subtree
            print(node.val, end=' ')                    # Visit current node
            self._inorder_rec(node.right)               # Traverse right subtree

    def preorder_traversal(self):
        """Perform a preorder traversal of the BST."""
        print("Preorder Traversal:")
        self._preorder_rec(self.root)

    def _preorder_rec(self, node):
        """Helper method for preorder traversal."""
        if node:
            print(node.val, end=' ')            # Visit current node 
            self._preorder_rec(node.left)       # Traverse left subtree
            self._preorder_rec(node.right)      # Traverse right subtree
            
    def postorder_traversal(self):
        """Perform a postorder traversal of the BST."""
        print("Postorder Traversal:")
        self._postorder_rec(self.root)

    def _postorder_rec(self, node):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_rec(node.left)      # Traverse left subtree
            self._postorder_rec(node.right)     # Traverse right subtree
            print(node.val, end=' ')            # Visit current node

    def find_min(self):
        """Find the minimum value in the BST."""
        if self.root is None:
            # If the tree is empty, there is no minimum value
            return None                         
        return self._find_min_rec(self.root)
    
    def _find_min_rec(self, node):
        """Helper method to find the minimum value recursively."""
        current = node
        while current.left is not None:         
            current = current.left              # Traverse to the leftmost node
        return current
    
    def find_max(self):
        """Find the maximum value in the BST."""
        if self.root is None:
            # If the tree is empty, there is no maximum value
            return None
        return self._find_max_rec(self.root)
    
    def _find_max_rec(self, node):
        """Helper method to find the maximum value recursively."""
        current = node
        while current.right is not None:
            current = current.right       # Traverse to the rightmost node
        return current
    
    def delete(self, key):
        """Delete a key from the BST."""
        # Call the recursive delete helper to remove the key from the BST
        self.root = self._delete_rec(self.root, key)        
        print(f"Deleted {key} from BST.")

    def _delete_rec(self, node, key):  
        """Helper method to delete a key recursively."""
        if node is None:
            return node                             # If the node is None, the key is not found
        
        if key < node.val:
            node.left = self._delete_rec(node.left, key)    # If key is less than current node's value, search in left subtree
        elif key > node.val:
            node.right = self._delete_rec(node.right, key)  # If key is greater than current node's value, search in right subtree
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right                           # If node has no left child, return right child 
            elif node.right is None:
                return node.left                            # If node has no right child, return left child
            
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
        left_height = self._height_rec(node.left)       # recursively find the height of left subtree
        right_height = self._height_rec(node.right)     # recursively find the height of right subtree
        return 1 + max(left_height, right_height)       # the height of the tree 1 more than the maximum height of left and right subtrees
    
    def clear(self):    
        """Clear the BST."""
        self.root = None    

    def __str__(self):
        """String representation of the BST."""
        return f"BST with root value: {self.root.val if self.root else 'None'}"
    
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

bst.delete(5)                                       # left child of root
print("Replaced by the node ",bst.root.left.val)
bst.delete(10)                                      # root itself
print("Replaced by the node ",bst.root.val)
bst.inorder_traversal()                             # Should print: 3 7 10 15
print()

print("Height of BST:", bst.height())  # Should print the height of the BST
    
print(bst)
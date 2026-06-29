# Binary Tree Post_order Traversal
# Qno.2 :- Given the root of a binary tree, return the post_order traversal of it's node's values

# Post_order traversal means: LEFT -> RIGHT -> ROOT
# We visit left subtree first, then right subtree, then the current node

# Definition for a binary tree node
from typing import List, Optional

class TreeNode:
    def __init__(self, val= 0, left= None, right= None):
        self.val = val          # The value stored in this node
        self.left = left        # Pointer to left child node
        self.right = right      # Pointer to right child node

class Solution:
    def postOrderTraversal(self, root):
        # We'll use two stacks to keep track of our traversal
        stack = [root]          # Stack to store nodes we need to process
        visit = [False]         # Stack to track if we've processed a node's children
        result = []             # List to store our final answer

        while stack: # Keep going until we've processed all nodes
            curr = stack.pop()  # Take the top node from stack (LIFO - Last In First Out)
            v = visit.pop()     # Check if this node is ready to be added to result

            if curr: # Only process if node exists (not None)
                if v:
                    # If v is True, it means we've already processed left and right children
                    # So now we can safely add this node to our result
                    result.append(curr.val)
                else:
                    # If v is False, we haven't processed this node's children yet
                    # We need to process in order: left -> right -> root
                    
                    # Step 1: Put the current node back on stack with v=True
                    # This means "next time we see this node, add it to result"
                    stack.append(curr)
                    visit.append(True)
                    
                    # Step 2: Add right child first (so it gets processed after left)
                    # Right child goes on stack with v=False (not ready yet)
                    if curr.right:
                        stack.append(curr.right)
                        visit.append(False)
                    
                    # Step 3: Add left child last (so it gets processed first)
                    # Left child goes on stack with v=False (not ready yet)
                    if curr.left:
                        stack.append(curr.left)
                        visit.append(False)
                            
        return result
    

# Let's create a simple binary tree to test our code
# Tree structure:
#       1
#      / \
#     3   2
# This should give us post_order_traversal: [3, 2, 1]

root = TreeNode(1)        # Create root node with value 1
root.left = TreeNode(3)   # Create left child with value 3
root.right = TreeNode(2)  # Create right child with value 2

sol = Solution()
print(sol.postOrderTraversal(root))  # Should print: [3, 2, 1]



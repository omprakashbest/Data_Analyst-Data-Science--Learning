#Qno.3: Given the root of a binary tree, return the pre_order traversal of it's nodes values. (iterate)
# pre_order :- root->left->right

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None , right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre_orderTraversal(self, root):
        # Initialize current_Node to root and empty stack
        currNode = root
        stack = []

        result = []
        
        # Continue while we have a current node OR stack is not empty
        while currNode or stack:  # while current node exists or stack is not empty
            if currNode:
                # Step 1: Process current_Node (ROOT) - add to result
                result.append(currNode.val)
                
                # Step 2: Push right child to stack for later processing
                # (We'll come back to it after processing left subtree)
                stack.append(currNode.right)
                
                # Step 3: Move to LEFT child (LEFT)
                currNode = currNode.left
            else:
                # When curr becomes None, pop from stack to get next node to process
                # This happens when we've finished processing a left subtree
                currNode = stack.pop()
        
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
print(sol.pre_orderTraversal(root))



# Minimum Distance between BST Nodes
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.


# In-Order Based (BST)
class Solution(object):
    def minDiffInBST(self, root):
        prev = None
        result = float("inf") 

        def dfs(currNode):
            if not currNode:
                return
            
            dfs(currNode.left)

            # Update result using the difference between current and previous node
            nonlocal prev, result
            
            if prev is not None:
                result = min(result, currNode.val - prev)
            prev = currNode.val

            dfs(currNode.right)
        dfs(root)
        return result


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
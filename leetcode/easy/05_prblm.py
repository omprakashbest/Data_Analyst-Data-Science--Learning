# Symmetric Tree
# Qno.05:-  Given the root of a binary tree , whether it is a mirror of itself(i.e., Symmetric around it's center)?

class Solutions:
    def isSymmetric(self, root)-> bool: # return type is boolean
        
        # Helper function to compare two nodes
        def dfs(left, right): # dfs :- depth first search 

            # Both nodes are None, so it's symmetric
            if not left and not right:
                return True
            # Only one node is None, not symmetric
            if not left or not right:
                return False
            # Check values and recurse on children in mirror order
            return (left.val == right.val and
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))

        # Start by comparing left and right subtree of root
        return dfs(root.left, root.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child
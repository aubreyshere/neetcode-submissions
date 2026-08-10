# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        # returns current max path at any point 
        def maxPaths(root) -> int:
            nonlocal maxSum
            if not root:
                return 0

            leftVal = max(0, maxPaths(root.left))
            rightVal = max(0, maxPaths(root.right))
            maxSum = max(root.val + leftVal + rightVal, maxSum)

            return root.val + max(leftVal, rightVal)

        maxPaths(root)
        
        return maxSum

        
        
        
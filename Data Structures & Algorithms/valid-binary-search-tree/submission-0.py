# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validBST(root, minVal, maxVal):
            if not root:
                return True
            elif not (minVal < root.val < maxVal):
                return False
            
            return validBST(root.left, minVal, root.val) and validBST(root.right, root.val, maxVal)

        return validBST(root, float("-inf"), float("inf"))


        
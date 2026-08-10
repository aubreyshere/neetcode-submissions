# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        def deathAdd(root, death) -> None:
            if not root:
                return
            if len(answer) <= death:
                answer.append([])
            answer[death].append(root.val)
            deathAdd(root.left, death + 1)
            deathAdd(root.right, death + 1)
            return

        deathAdd(root, 0)

        return answer

            

        
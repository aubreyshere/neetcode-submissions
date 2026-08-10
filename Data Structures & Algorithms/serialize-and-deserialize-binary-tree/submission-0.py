# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        else:
            return f"{root.val}-{self.serialize(root.left)}-{self.serialize(root.right)}"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split("-")
        print(nodes)
        index = 0

        def rebuild(root) -> Optional[TreeNode]:
            nonlocal index
            if nodes[index] == 'N':
                index += 1
                return None
            root.val = nodes[index]
            index += 1

            root.left = rebuild(TreeNode())
            root.right = rebuild(TreeNode())
            return root

        tree = rebuild(TreeNode())

        return tree



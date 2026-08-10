"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        used = {}

        def cloneNodes(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            elif node.val in used:
                return used[node.val]

            clone = Node(node.val)
            used[clone.val] = clone
            for i, n in enumerate(node.neighbors):
                newNode = cloneNodes(n)
                clone.neighbors.append(newNode)

            return clone

        root = cloneNodes(node)

        return root
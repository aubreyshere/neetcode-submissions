"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMapping = {}

        def copyNode(head) -> 'Optional[Node]':
            if head in nodeMapping:
                return nodeMapping[head]
            elif head is None:
                return None
            
            newNode = Node(head.val)
            nodeMapping[head] = newNode
            newNode.next= copyNode(head.next)
            newNode.random = copyNode(head.random)

            return newNode

        copyNode(head)

        return nodeMapping.get(head, None)
        
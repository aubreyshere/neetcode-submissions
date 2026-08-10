# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        prev = None
        distance = 0

        while p2:
            if distance < n:
                p2 = p2.next
                distance += 1
            else:
                prev = p1
                p2 = p2.next
                p1 = p1.next

        if head == p1:
            return p1.next
        elif distance < n:
            return head

        prev.next = p1.next

        return head
        


        
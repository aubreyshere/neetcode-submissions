# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        remainder = 0

        while True:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            cur.val = (val1 + val2 + remainder) % 10
            remainder = (val1 + val2 + remainder) // 10
            
            if l1 is None and l2 is None and remainder == 0:
                break;
            cur.next = ListNode()
            cur = cur.next
            
        return res
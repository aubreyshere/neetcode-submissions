# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return

        slow = head
        fast = head

        # get slow to midway
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse starting at slow + 1
        current = slow.next
        prev = None
        while current:
            future = current.next
            current.next = prev
            prev = current
            current = future

        slow.next = None
        slow = prev

        # merge
        fast = head
        while slow:
            temp = slow.next
            slow.next = fast.next
            fast.next = slow
            slow = temp
            fast = fast.next.next


            
            






        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head1 = None

        for head2 in lists:
            newList = main = ListNode()

            while head1 and head2:
                if head1.val < head2.val:
                    newList.next = head1
                    head1 = head1.next
                else:
                    newList.next = head2
                    head2 = head2.next
                
                newList = newList.next

            newList.next = head1 or head2
            head1 = main.next

        return head1

        
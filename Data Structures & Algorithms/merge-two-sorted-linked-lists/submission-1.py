# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        newList = None
        firstNode = None

        while head1 != None or head2 != None:
            if head1 == None:
                nextNode = head2
                head2 = head2.next
            elif head2 == None:
                nextNode = head1
                head1 = head1.next
            elif head1.val < head2.val:
                nextNode = head1
                head1 = head1.next
            else:
                nextNode = head2
                head2 = head2.next
            
            if newList == None:
                newList = nextNode
                firstNode = newList
            else:
                newList.next = nextNode
                newList = nextNode

        return firstNode
        
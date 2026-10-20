# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1=ListNode(0)
        prev1=dummy1
        dummy2=ListNode(0)
        prev2=dummy2
        curr=head
        while curr!=None:
            if curr.val<x:
                prev1.next=curr
                prev1=prev1.next
            else:
                prev2.next=curr
                prev2=prev2.next
            curr=curr.next
        prev2.next=None
        prev1.next=dummy2.next
        head=dummy1.next
        return head

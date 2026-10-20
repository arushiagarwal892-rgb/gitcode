# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        for _ in range(k-1):
            if fast==None:
                return None
            fast=fast.next
        curr=fast.next
        while curr:
            curr=curr.next
            slow=slow.next
        temp=slow.val
        slow.val=fast.val
        fast.val=temp
        return head
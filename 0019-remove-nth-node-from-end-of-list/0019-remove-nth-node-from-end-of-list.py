# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr=head
        l=0
        while curr!=None:
            curr=curr.next
            l=l+1
        t=l-n
        curr=head
        if t == 0:
            return head.next
        for i in range (t-1):
            if curr.next!=None and curr.next.next!=None:
                curr=curr.next
        curr.next=curr.next.next
        return head


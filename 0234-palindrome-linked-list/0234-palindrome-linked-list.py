# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        a=[]
        b=[]
        if head==None or head.next==None:
            return True
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            a.append(slow.val)
            slow=slow.next
        while slow:
            b.append(slow.val)
            slow=slow.next
        if len(a)!=len(b):
            b=b[1::]
        if a==b[::-1]:
            return True
        return False
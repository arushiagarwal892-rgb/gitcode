# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        temp=head
        if head==None or head.next==None:
            return None
        while fast!=None  and fast.next!=None:
            fast=fast.next.next
            if slow==head:
                temp=head
            else:
                temp=temp.next
            slow=slow.next
        temp.next=slow.next
        return head
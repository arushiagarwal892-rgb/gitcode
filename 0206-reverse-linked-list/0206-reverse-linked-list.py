# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        temp=head
        temp2=temp.next
        temp3=temp2.next
        while temp3 is not None:
            temp2.next=temp
            temp=temp2
            temp2=temp3
            temp3=temp3.next
        temp2.next=temp
        head.next=None
        head=temp2
        return head

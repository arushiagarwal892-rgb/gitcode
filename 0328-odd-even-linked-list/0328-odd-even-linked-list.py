# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        dummy1=ListNode(0)
        curr1=dummy1
        dummy2=ListNode(0)
        curr2=dummy2
        curr=head
        pos=1
        while curr:
            if pos%2==0:
                curr2.next=curr
                curr2=curr2.next
            else:
                curr1.next=curr
                curr1=curr1.next
            curr=curr.next
            pos=pos+1
        curr2.next=None
        curr1.next=dummy2.next
        return dummy1.next
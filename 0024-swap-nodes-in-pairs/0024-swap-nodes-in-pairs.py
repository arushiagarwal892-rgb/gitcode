# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        prev=None
        if head == None or head.next == None:
            return head
        head=temp.next
        while temp!=None and temp.next!=None:
            temp2=temp.next
            temp.next=temp2.next
            temp2.next=temp
            if prev!=None:
                prev.next=temp2
            prev=temp
            temp=temp.next
        return head
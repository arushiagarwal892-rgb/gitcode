# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # 2,067,718

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1=head
        curr2=head
        while curr2!=None and curr2.next!=None:
            curr1=curr1.next
            curr2=curr2.next.next
        return curr1

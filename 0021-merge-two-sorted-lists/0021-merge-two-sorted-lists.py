# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        curr=dummy
        temp1=list1
        temp2=list2
        while temp1!=None and temp2!=None:
            if temp1.val<=temp2.val:
                curr.next=ListNode(temp1.val)
                curr=curr.next
                temp1=temp1.next
            else:
                curr.next=ListNode(temp2.val)
                curr=curr.next
                temp2=temp2.next
        while temp1!=None:
            curr.next=ListNode(temp1.val)
            curr=curr.next
            temp1=temp1.next
        while temp2!=None:
            curr.next=ListNode(temp2.val)
            curr=curr.next
            temp2=temp2.next
        return dummy.next
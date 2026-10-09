# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n1=0
        n2=0
        temp1=l1
        temp2=l2
        while temp1!=None:
            n1=n1*10+temp1.val
            temp1=temp1.next
        while temp2!=None:
            n2=n2*10+temp2.val
            temp2=temp2.next
        n=str(n1+n2)
        dummy=ListNode(0)
        temp=dummy
        for i in n:
            temp.next=ListNode(int(i))
            temp=temp.next
        return dummy.next
        

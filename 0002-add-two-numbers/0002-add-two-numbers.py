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
        s1=''
        s2=''
        temp1=l1
        temp2=l2
        while temp1!=None:
            v=str(temp1.val)
            temp1=temp1.next
            s1=v+s1
        while temp2!=None:
            v=str(temp2.val)
            s2=v+s2
            temp2=temp2.next
        sum=str(int(s1)+int(s2))[::-1]
        dummy=ListNode(0)
        current=dummy
        for i in sum:
            current.next=ListNode(int(i))
            current=current.next
        return dummy.next

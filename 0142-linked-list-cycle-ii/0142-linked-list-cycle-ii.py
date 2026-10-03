# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ind=head
        slow=head
        fast=head
        flag=False
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                flag=True
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                t=slow
                break
        if flag==False:
            return None
        while ind!=None:
            if ind==t:
                return slow
            ind=ind.next
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.new_node=Node(val)
        temp=self.head
        self.new_node.next=temp
        self.head=self.new_node
        self.size=self.size+1
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.new_node=Node(val)
        temp=self.head
        if temp is None:
            self.head = self.new_node
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=self.new_node
        self.size=self.size+1
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        self.new_node=Node(val)
        temp=self.head
        if index==0:
            self.new_node.next=self.head
            self.head=self.new_node
            self.size=self.size+1
            return
        for _ in range(index-1):
            temp=temp.next
        self.new_node.next=temp.next
        temp.next=self.new_node
        self.size=self.size+1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
        self.size=self.size-1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
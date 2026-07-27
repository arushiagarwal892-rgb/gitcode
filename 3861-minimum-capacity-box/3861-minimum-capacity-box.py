class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        # [1,3,5,7]
        item=capacity[:]
        item.sort()
        for i in item:
            if i>=itemSize:
                return capacity.index(i)
        return -1
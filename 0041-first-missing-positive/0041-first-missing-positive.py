class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        i=1
        while i in s:
            i=i+1
        return i
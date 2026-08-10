class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range (len(nums)):
            if nums[i]==val:
                nums[i]='_'
            else:
                k=k+1
        nums.sort()
        return k
        
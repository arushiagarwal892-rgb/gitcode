class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        sum=0
        right=k-1
        for i in range (0,k):
            sum=sum+nums[i]
        maxi=sum
        while right<len(nums)-1:
            right=right+1
            left=left+1
            sum=sum+nums[right]-nums[left-1]
            maxi=max(maxi,sum)
        return float(maxi)/k

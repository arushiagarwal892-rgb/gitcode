class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        for i in range (len(nums)-1):
            if nums[i]+1==nums[i+1]:
                sum=sum+nums[i+1]
            else:
                break
        while True:
            if sum not in nums:
                return sum
            else:
                sum=sum+1
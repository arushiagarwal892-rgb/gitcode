class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        sum2=0
        for i in range (len(nums)-1):
            if nums[i]<nums[i+1]:
                sum1=sum1+nums[i]
            else:
                break
        sum1=sum1+nums[i]
        for j in range (i,len(nums)):
            sum2=sum2+nums[j]
        if sum1>sum2:
            return 0
        elif sum1<sum2:
            return 1
        else:
            return -1
        

class Solution(object):
    def countValidSubarrays(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        count=0
        sum=0
        x=str(x)
        for i in range (0,len(nums)):
            for j in range (i,len(nums)):
                sum=sum+nums[j]
                su=str(sum)
                if su[0]==x and su[-1]==x:
                    count=count+1
            sum=0
        return count
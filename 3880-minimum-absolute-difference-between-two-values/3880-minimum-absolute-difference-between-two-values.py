class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in range (len(nums)):
            if nums[i]==1:
                for j in range (len(nums)):
                    if nums[j]==2:
                        ans.append(abs(i-j))
        if ans:
            return min(ans)
        return -1

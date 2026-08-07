class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[0]*(len(nums)+1)
        ans[0]=1
        for i in range (len(nums)):
            ans[nums[i]]=ans[nums[i]]+1
        return [i for i, x in enumerate(ans) if x == 0]
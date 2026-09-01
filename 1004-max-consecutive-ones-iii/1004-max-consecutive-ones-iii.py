class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        mle=0
        count=0
        while r<len(nums):
            if nums[r]==0:
                count=count+1
                while count>k:
                    if nums[l]==0:
                        count=count-1
                    l=l+1
            r=r+1
            mle=max(mle,r-l)
        return mle

class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        ans=0
        for i in nums:
            i=str(i)
            ans=ans+i.count(str(digit))
        return ans


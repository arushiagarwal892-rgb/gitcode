class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans=[0]*(len(nums)+1)
        ans[0]=1
        for i in nums:
            ans[i]=ans[i]+1
        return [ans.index(2),ans.index(0)]


        
            
        
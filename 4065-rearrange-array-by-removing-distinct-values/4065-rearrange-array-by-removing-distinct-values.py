class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        num1=nums[:]
        l=len(nums)
        while len(ans)!=l:
            s1=set(num1)
            s1=list(s1)
            s1.sort()
            for i in s1:
                ans.append(i)
                nums.remove(i)
            num1=nums[:]
        return ans
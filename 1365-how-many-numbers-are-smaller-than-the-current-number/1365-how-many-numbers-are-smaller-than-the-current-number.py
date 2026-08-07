class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        coun=[]
        for i in range (len(nums)):
            for j in range (0,len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            coun.append(count)
            count=0
        return coun
            
                
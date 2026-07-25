class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        flag1=True
        flag2=True
        ans.append(nums[0])
        for i in range (1,len(nums)):
            for j in range (0,i):
                if nums[j]>=nums[i]:
                    flag1=False
                    break
            if flag1==True:
                ans.append(nums[i])
            else:
                for j in range (i+1,len(nums)):
                    if nums[j]>=nums[i]:
                        flag2=False
                        break
                if flag2==True:
                    ans.append(nums[i])
            flag2=True
            flag1=True
        return ans



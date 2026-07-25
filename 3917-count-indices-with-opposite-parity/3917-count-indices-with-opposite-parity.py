class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        score=0
        ans=[]
        for i in range (0,len(nums)-1):
            od=nums[i]%2
            for j in range (i+1,len(nums)):
                if od==0:
                    if nums[j]%2!=0:
                        score=score+1
                else:
                    if nums[j]%2==0:
                        score=score+1
            ans.append(score)
            score=0
        ans.append(0)
        return ans
            
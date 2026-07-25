class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums1=[]
        nums2=[]
        stable=[]
        for i in range (0,len(nums)):
            nums1=nums[0:i+1]
            nums2=nums[i:]
            t=max(nums1)-min(nums2)
            stable.append(t)
            nums1=[]
            nums2=[]
        for i in stable:
            if i<=k:
                return stable.index(i)
        return -1

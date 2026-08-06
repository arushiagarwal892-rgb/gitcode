class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3=nums1+nums2
        num3.sort()
        l=(len(num3))
        if (l)%2!=0:
            return num3[l//2]
        else:
            return ((num3[(l//2)-1]+num3[l//2])/2.0)


        
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        if len(arr)==2:
            return True
        for i in range (len(arr)-2):
            if arr[i]-arr[i+1]!=arr[i+1]-arr[i+2]:
                return False
        return True
                
class Solution(object):
    def gcd(self,max1,min1):
            if min1==0:
                return max1
            return self.gcd(min1,max1%min1)
    def findGCD(self, nums):
        max1=max(nums)
        min1=min(nums)
        return self.gcd(max1,min1)
        
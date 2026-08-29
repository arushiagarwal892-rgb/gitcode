class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m=str(n)
        sum=0
        product=1
        for i in m:
            sum=sum+int(i)
            product=product*int(i)
        if n%(sum+product)==0:
            return True
        else:
            return False
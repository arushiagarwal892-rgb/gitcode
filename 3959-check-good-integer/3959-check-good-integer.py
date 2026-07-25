class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sqsum=0
        sum=0
        n=str(n)
        for i in n:
            sqsum=sqsum+int(i)*int(i)
            sum=sum+int(i)
        if sqsum-sum>=50:
            return True
        else:
            return False
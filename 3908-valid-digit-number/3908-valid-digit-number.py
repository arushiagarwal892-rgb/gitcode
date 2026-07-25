class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        s=str(n)
        x=str(x)
        if s[0]==x:
            return False
        elif x in s:
                return True
        else:
            return False
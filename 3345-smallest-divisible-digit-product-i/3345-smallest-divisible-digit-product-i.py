class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            p=1
            n=str(n)
            for i in n:
                p=int(i)*p
            if p%t==0:
                return int(n)
            n=int(n)+1
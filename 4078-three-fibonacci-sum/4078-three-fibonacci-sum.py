class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fibb=[0,1,1]
        while fibb[-1]<=n:
            m=fibb[-1]
            k=fibb[-2]
            fibb.append(m+k)
        for i in range(0,len(fibb)-2):
            if n==fibb[i]+fibb[i+1]+fibb[i+2]:
                return True
        return False



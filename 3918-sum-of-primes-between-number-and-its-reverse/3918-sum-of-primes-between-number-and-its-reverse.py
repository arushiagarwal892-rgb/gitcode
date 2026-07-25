class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=str(n)
        r=int(t[::-1])
        flag="true"
        sum=0
        for i in range (min(n,r),max(n,r)+1):
            for j in range (2,i):
                if i%j==0:
                    flag="false"
            if flag=="true" and i!=1:
                sum=sum+i
            flag="true"
        return sum


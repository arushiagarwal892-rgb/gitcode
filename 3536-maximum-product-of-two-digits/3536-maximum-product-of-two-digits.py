class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        m=[]
        for i in n:
            m.append(int(i))
        m.sort(reverse=True)
        mult=m[0]*m[1]
        return mult

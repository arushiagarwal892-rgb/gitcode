class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        su=0
        count=0
        for i in s:
            su= su*2+int(i)
        while su!=1:
            if su%2==0:
                su=su/2
            else:
                su=su+1
            count=count+1
        return count
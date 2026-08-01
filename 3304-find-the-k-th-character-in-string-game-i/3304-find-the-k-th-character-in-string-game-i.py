class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        s="a"
        while len(s)<k:
            for i in s:
                if ord(i)<122:
                    ch=ord(i)+1
                else:
                    ch=97
                s=s+chr(ch)
        return s[k-1]
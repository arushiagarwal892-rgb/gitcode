class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        l=0
        n=0
        hash=[-1]*256
        while r<len(s):
            o=ord(s[r])
            if hash[o]!=-1:
                if hash[o]>=l:
                    l=hash[o]+1
            le=r-l+1
            n=max(n,le)
            hash[o]=r
            r=r+1
        return n
            
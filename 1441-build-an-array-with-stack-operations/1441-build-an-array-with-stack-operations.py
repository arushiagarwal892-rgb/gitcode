class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        ans2=[]
        for i in range (1,n+1):
            ans.append(i)
            ans2.append("Push")
            if i not in target:
                ans.remove(i)
                ans2.append("Pop")
            if target==ans:
                return ans2

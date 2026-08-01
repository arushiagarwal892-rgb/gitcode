class Solution(object):
    def evenel (self,n):
        if n==1:
            return 1
        
        return 2*self.oddel(n//2)


    def oddel (self,n):
        if n == 1:
            return 1
        if n%2==1:
                return 2*self.evenel(n//2)
        else:
                return 2*self.evenel(n//2)-1
    def lastRemaining(self, n):
        return self.evenel (n)
        
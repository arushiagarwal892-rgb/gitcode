class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=0
        binary=str(bin(n)[2:])
        for i in range (len(binary)-1):
            if binary[i]=="1" and binary[i+1]=="1":
                count=count+1
        if count==1:
            return True
        else:
            return False

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num))!=1:
            an=0
            num=str(num)
            for i in num:
                an=an+int(i)
            num=an
        return num


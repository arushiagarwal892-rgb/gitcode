class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        bl=""
        ar=[0,0]
        for i in moves:
            if i=="L":
                ar[0]=ar[0]-1
            elif i=="R":
                ar[0]=ar[0]+1
            elif i=="D":
                ar[1]=ar[1]-1
            elif i=="U":
                ar[1]=ar[1]+1
            else:
                bl=bl+"_"
        if ar[0]<=0:
            ar[0]=ar[0]-len(bl)
        else:
            ar[0]=ar[0]+len(bl)
        return (abs(ar[0])+abs(ar[1]))
                
                    
                
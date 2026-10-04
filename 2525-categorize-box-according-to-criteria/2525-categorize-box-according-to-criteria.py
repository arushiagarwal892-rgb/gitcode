class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        t=''
        b=''
        if length>=10000 or height>=10000 or width>=10000 or height*length*width>=1000000000:
            t=t+'Bulky'
        if mass>=100:
            b=b+'Heavy'
        if t=='Bulky' and b=='Heavy':
            return 'Both'
        elif t=='' and b=='':
            return 'Neither'
        elif t=='Bulky' and b=='':
            return t
        else:
            return b
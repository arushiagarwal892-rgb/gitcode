class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator

        ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
            }
        l=[]
        for i in tokens:
            if i not in ops:
                l.append(int(i))
            else:
                b= l.pop()
                a = l.pop()

                t = ops[i](a, b)
                l.append(int(t))
        return l[0]
            
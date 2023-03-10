class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ack = []
        lookfor = {')':'(', '}':'{', ']':'['}

        for p in s:
            if p in lookfor.values():
                ack.append(p)
            elif ack and lookfor[p] == ack[-1]:
                ack.pop()
            else:
                return False

        return ack == []
        
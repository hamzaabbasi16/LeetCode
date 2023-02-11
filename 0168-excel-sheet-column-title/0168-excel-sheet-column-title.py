class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        return "" if columnNumber == 0 else self.convertToTitle((columnNumber - 1) / 26) + chr((columnNumber - 1) % 26 + ord('A'))
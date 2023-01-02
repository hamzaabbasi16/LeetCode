class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.capitalize():
            return True
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        return False
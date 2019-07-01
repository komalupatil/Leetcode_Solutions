class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        for i in range(len(s)-1,-1,-1):
            string += s[i]
        return string
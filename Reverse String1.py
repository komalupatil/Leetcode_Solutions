class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s)-1
        string2 = ""
        while(i>=0):
            string2 = string2 + s[i]
            i = i-1
        return string2
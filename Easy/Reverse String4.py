class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        string = ""
        for i in range(len(s)):
            stack.append(s[i])
        for j in range(len(stack)):
            string += stack.pop()
        return string
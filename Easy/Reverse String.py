#leetcode 344. Reverse String
#solution1

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

#solution2

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

#solution3

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s[::-1]
        return s


#solution4
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

#Solution5
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        
        while (l<r):
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l+=1
            r-=1
        return s
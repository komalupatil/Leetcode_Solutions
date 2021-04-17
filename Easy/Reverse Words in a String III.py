#Leetcode 557. Reverse Words in a String III

#Solution1
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s)

#Solution2
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))

#Solution3
class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i for i in s]
        start = 0
        end = 0
        while end<len(s):

            while s[end] != " " and end != len(s)-1:
                end += 1

            if end == len(s)-1:
                right = len(s)-1
            else:
                right = end-1

            left = start
            
            while left< right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp

                left += 1
                right -= 1

            start = end + 1
            end = end + 1
            
        return "".join([i for i in s])
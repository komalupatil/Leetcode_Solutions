# Leetcode 709. To Lower Case

#Solution1
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

#Solution2
class Solution:
    def toLowerCase(self, str: str) -> str:
        char = []
        for c in str:
            if "A" <= c <= "Z":
                char.append(chr(ord(c)+32))
            else:
                char.append(c)
        return "".join(c for c in char)

#Solution3
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c)+32) if "A" <= c <= "Z" else c for c in str)

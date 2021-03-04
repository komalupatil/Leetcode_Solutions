#Leetcode 925. Long Pressed Name

#Topic: Two Pointers

#Solution


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        
        n = len(name)
        m = len(typed)
        
        while j<m:
            if i<n and name[i] == typed[j]:
                i+=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j+=1
        return i==n
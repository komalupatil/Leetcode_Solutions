#Leetcode 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        result = ""
        while p1< len(word1) and p2< len(word2):
            result += word1[p1]
            result += word2[p2]
            p1+=1
            p2+=1
        while p1 < len(word1):
            result += word1[p1]
            p1+=1
        while p2< len(word2):
            result += word2[p2]
            p2+=1
        return result
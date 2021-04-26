#Leetcode 819. Most Common Word

#Solution
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        dict1 = dict()
        count = 0
        result = " "
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in dict1:
                dict1[word] +=1
            else:
                dict1[word] = 1
            if dict1[word] > count:
                count = dict1[word]
                result = word
        return result
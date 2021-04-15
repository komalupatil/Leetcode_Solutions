#Leetcode 1773. Count Items Matching a Rule

#Solution

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type": 
            i = 0
        if ruleKey == "color":
            i = 1
        if ruleKey == "name":
            i = 2
        count = 0 
        for j in range(len(items)):
            if items[j][i] == ruleValue:
                count += 1
        return count
#Leetcode 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        
        repeated = []

        for i in range(len(s)-9):
            subSequence = s[i:i+10]
            if subSequence in seen:
                seen[subSequence] += 1
            else:
                seen[subSequence] = 1
            if seen[subSequence] == 2:
                repeated.append(subSequence)
        return repeated     
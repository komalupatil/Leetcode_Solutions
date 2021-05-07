#Leetcode 771. Jewels and Stones

class Solution1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for i in S:
            if i in J:
                cnt +=1 
        return cnt

class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for i in S if i in J)

class Solution3:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)

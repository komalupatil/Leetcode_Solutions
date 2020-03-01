#leetcode771. Jewels and Stones
#solution1
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for i in S:
            if i in J:
                cnt +=1 
        return cnt

#solution2
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for i in S if i in J)

#solution3
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)

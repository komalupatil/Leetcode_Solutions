#Leetcode 1295. Find Numbers with Even Number of Digits

class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            lis = list(map(int, str(i)))
            if len(lis)%2 == 0:
                result +=1
            else:
                continue
        return result


class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
         return len([x for x in nums if len(str(x)) % 2 == 0])
            

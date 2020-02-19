#leetcode66 plus one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        l = len(digits)
        string = ''.join(str(i) for i in digits)
        intPlusOne = int(string) + 1
        string = str(intPlusOne)
        for i in string:
            result.append(int(i))
        return result

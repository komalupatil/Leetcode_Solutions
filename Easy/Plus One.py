#Leetcode 66. plus one

class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        l = len(digits)
        string = ''.join(str(i) for i in digits)
        intPlusOne = int(string) + 1
        string = str(intPlusOne)
        for i in string:
            result.append(int(i))
        return result

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return []
        
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1
            
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits

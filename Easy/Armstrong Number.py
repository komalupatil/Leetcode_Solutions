#Leetcode 1134. Armstrong Number

class Solution1:
    def isArmstrong(self, N: int) -> bool:
        result = 0
        for i in str(N):
            result += int(i) ** len(str(N)))  #or using pow() function from import math
        return result == N
        
            
obj = Solution()
result = obj.isArmstrong(153)
result1 = obj.isArmstrong(123)
print(result)
print(result1)


class Solution2:
    def isArmstrong(self, N: int) -> bool:
        temp = N
        total = 0
        k = len(str(N))  #another way to calculate length of given number is "k = math.floor(math.log10(N)) + 1 ".
        while temp:
            digit = temp%10
            total += digit ** k
            temp //= 10
        return total == N

#Leetcode 1134. Armstrong Number

#The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
#Given a positive integer N, return true if and only if it is an Armstrong number.
#Example-1
#Input: 153
#Output: true
#Explanation: 
#153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

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

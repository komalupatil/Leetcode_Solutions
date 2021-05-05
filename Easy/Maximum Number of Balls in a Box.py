#Leetcode 1742. Maximum Number of Balls in a Box

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def numberSum(number):
            sum1 = 0
            while number:
                sum1 += number%10
                number = number//10
            return sum1
        
        d = collections.defaultdict(int)
        
        for i in range(lowLimit, highLimit+1):
            hashVal = numberSum(i)
            d[hashVal] +=1
            
        return max(d.values())
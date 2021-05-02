#Leetcode 762. Prime Number of Set Bits in Binary Representation

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime_set = {2,3,5,7,11,13,17,19}
        
        result = 0
        
        for i in range(L, R+1):
            one_cnt = bin(i).count('1')
            if one_cnt in prime_set:
                result += 1
        return result
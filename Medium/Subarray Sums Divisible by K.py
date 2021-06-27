#Leetcode 974. Subarray Sums Divisible by K

#Prefix Sum
#prefix_sum(i,j)%k = sum(0,j)%k - sum(0,i-1)%k  (%k for divisible by k)
#0 = sum(0,j)%k - sum(0,i-1)%k
#sum(0,j)%k = sum(0,i-1)%k
#k = sum(0,j) - sum(0,i-1)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {}
        count, contSum = 0,0
        d[0] = 1
        for i in range(len(nums)):
            contSum += nums[i]
            remainder = contSum % k
            if remainder in d:
                count += d[remainder]
            d[remainder] = d.get(remainder, 0)+1
        
        return count
            
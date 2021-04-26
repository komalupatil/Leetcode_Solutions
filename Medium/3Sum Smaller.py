#Leetcode 259. 3Sum Smaller

#Given an array of n integers nums and a target, 
#find the number of index triplets i, j, k with 0 <= i < j < k < n that 
#satisfy the condition nums[i] + nums[j] + nums[k] < target.
#Ex 1:
#Input:  nums = [-2,0,1,3], target = 2
#Output: 2
#Explanation:
#Because there are two triplets which sums are less than 2:
#[-2, 0, 1]
#[-2, 0, 3]


#Solution
class Threesum:
    def solution(self, nums, target):
        
        result = 0
        nums.sort()

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            while j<k:
                s = nums[i]+nums[j]+nums[k]

                if s >= target:
                    k-=1
                else:
                    result += (k-j)
                    j+=1
        return result
    

solve = Threesum()

nums = [-2,0,1,3]
target = 2
solve1 = solve.solution(nums, target)
print(solve1)
nums1 = [5,1,3,4,7]
target1 = 12
solve2 = solve.solution(nums1, target1)
print(solve2)
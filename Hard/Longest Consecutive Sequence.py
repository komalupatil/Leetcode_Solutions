#Leetcode 128. Longest Consecutive Sequence

#TLE
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_seq = 0
        for num in nums:
            cur_num = num
            cur_seq = 1
            while cur_num +1 in nums:
                cur_num +=1
                cur_seq +=1
            
            max_seq = max(max_seq, cur_seq)
        return max_seq

#Sorting
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        max_streak = 1
        curr_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] +1:
                    curr_streak += 1
                else:
                    max_streak = max(max_streak, curr_streak)
                    curr_streak = 1
        return max(max_streak, curr_streak)

#set
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_streak = 0
        nums = set(nums)
        
        for num in nums:
            if num-1 not in nums:
                curr_streak = 1
                curr_num = num
                
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
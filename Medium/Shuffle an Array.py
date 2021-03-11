#Leetcode 384. Shuffle an Array

#Solution1

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = list(self.nums)
        for i in range(len(ans)-1):
            j = random.randrange(i, len(ans))
            ans[i], ans[j] = ans[j], ans[i]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

#Solution2

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = list(self.nums)
        for i in range(len(ans)-1, 0, -1):
            j = random.randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
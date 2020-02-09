#leetcode 904 
#similar to leetcode problem 340
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if (len(tree) <= 2):
            return len(tree)
        winStart = 0
        maxLength = 0
        fruit_freq = {}
        for winEnd in range(len(tree)):
            right_fruit = tree[winEnd]
            if right_fruit not in fruit_freq:
                fruit_freq[right_fruit] = 0
            fruit_freq[right_fruit] += 1  
            while len(fruit_freq) > 2:
                fruit_freq[tree[winStart]] -= 1
                if fruit_freq[tree[winStart]] == 0:
                    del fruit_freq[tree[winStart]]
                winStart +=1
            maxLength = max(maxLength, winEnd-winStart +1)
        return maxLength

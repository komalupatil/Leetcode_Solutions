#leetcode 1165. Single-Row Keyboard

#Solution1
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        j = 0
        time = 0
        lookup = {val:i for i, val in enumerate(keyboard)}
        for  c in word:
            time += abs(lookup[c] - j)
            j = lookup[c]
        return time

#solution2 - without using dictionary
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cur_index = 0
        time = 0
        for  c in word:
            next_index = keyboard.index(c)
            time += abs(next_index - cur_index)
            cur_index = next_index
        return time



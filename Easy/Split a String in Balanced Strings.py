#Leetcode 1221. Split a String in Balanced Strings

#Solution1


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = 0
        for char in s:
            count += char == 'L'
            count -= char == 'R'
            result += count == 0
        return result


#Solution2 using accumulate function and list comprehension

from itertools import accumulate as acc
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        return list(acc(1 if c == "R" else -1 for c in s)).count(0)

#Solution3

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        substrings = l_count = r_count = 0
        
        for i in s:
            if i == 'L':
                l_count += 1
            if i == "R":
                r_count += 1
            if l_count == r_count:
                substrings += 1
        return substrings
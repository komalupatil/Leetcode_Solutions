# Leetcode 13. Roman to Integer


"""
Given Details: 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

"""

class Solution1:
    def romanToInt(self, s: str) -> int:
        roman_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,   "D": 500, "M": 1000}
        numerical_value = 0
        for i in range(len(s)):
            if i > 0 and roman_value[s[i]] > roman_value[s[i-1]]:
                numerical_value += roman_value[s[i]] -2 * roman_value[s[i-1]]
            else: 
                numerical_value += roman_value[s[i]]
        return numerical_value



class Solution2:
    def romanToInt(self, s: str) -> int:
        # make dict of existing roman to integer values
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # if length of given string is 1 then just return its equivalent integer value from dict
        if len(s) == 1:
            return symbols[s[0]]
        
        # if len of string is 0 rthen return 0
        if len(s) == 0:
            return 0
        
        num = 0
        i = 0
        while i < len(s):
            current_char = symbols[s[i]]
            next_char = 0

            # check if index goes out of range before checking next element
            if i+1 < len(s):
                next_char = symbols[s[i+1]]

            # check if next character is greater than current, if yes then subtract next from current
            if current_char < next_char:
                num = num + (next_char - current_char)
                i += 2
            else: 
                # else keep adding integr values one by one
                num = num + current_char
                i += 1
            
        return num
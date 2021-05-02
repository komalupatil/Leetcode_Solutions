#Leetcode 1694. Reformat Phone Number

class Solution:
    def reformatNumber(self, number: str) -> str:
        result = []
        
        number = number.replace("-", "").replace(" ", "")
        
        for i in range(0, len(number), 3):
            if i+4 != len(number):
                result.append(number[i:i+3])
            else:
                result.extend([number[i:i+2], number[i+2:]])
                break
        return "-".join(result)
#leetcode 1588. Sum of All Odd Length Subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        for i in range(len(arr)):
            start = n-i
            end = i+1
            total = start * end
            odd = (total+1)//2
            result += odd*arr[i]
        return result
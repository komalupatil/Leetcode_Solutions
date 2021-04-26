#Leetcode 1539. Kth Missing Positive Number

#Solution - linear search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)
        for i in range(1, k+len(arr)+1):
            if i not in set_arr:
                k-=1
            if k == 0:
                return i

#Solution - binary search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k
        if k == 0:
            return 0
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] - (mid+1) <k:
                low = mid+1
            else:
                high = mid - 1
        return low + k  #(arr[high]+k - (arr[high]-(high+1))) and low = high + 1 when low > high (when low and high cross each other in low<= high condition)
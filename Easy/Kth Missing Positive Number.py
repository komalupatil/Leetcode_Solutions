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

#Solution - binary search (check this)
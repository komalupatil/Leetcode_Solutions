#Leetcode 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = collections.Counter(arr)
        
        if s[0] > 1:  #check if duplicate zeroes are there
            return True
        
        for num in arr:
            if s[2*num] and num!=0:
                return True
        return False
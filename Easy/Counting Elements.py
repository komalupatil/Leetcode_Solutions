#Leetcode 1426. Counting Elements
#Problem7 from 30 day leetcoding challenge - new problem introduced by leetcode 
#Given an integer array arr, count element x such that x + 1 is also in arr.
#If there're duplicates in arr, count them seperately.
#Example 1:
#Input: arr = [1,2,3]
#Output: 2
#Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
#Example 2:
#Input: arr = [1,1,3,3,5,5,7,7]
#Output: 0
#Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
#Example 3:
#Input: arr = [1,3,2,3,5,0]
#Output: 3
#Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
#Example 4:
#Input: arr = [1,1,2,2]
#Output: 2
#Explanation: Two 1s are counted cause 2 is in arr.
#Constraints:
#1 <= arr.length <= 1000
#0 <= arr[i] <= 1000


class Solution1:
    def countElements(self, arr: List[int]) -> int:
        
        count = 0
        for num in arr:
            if num+1 in arr:
                count +=1
            else:
                continue
        return count

#(using hashset)
class Solution2:
    def countElements(self, arr: List[int]) -> int:
        output = set(arr)
        count = 0
        for num in arr:
            if num+1 in output:
                count+=1
            else:
                continue
        return count

#(using dictionary)
class Solution3:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = 1
        count = 0
        for x in arr:
            if x+1 in d:
                count+=1
        return count

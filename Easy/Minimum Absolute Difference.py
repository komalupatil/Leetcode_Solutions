#Leetcode 1200. Minimum Absolute Difference

class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float('inf')
        dicDiff = collections.defaultdict(list)
        arr.sort()
        
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            dicDiff[diff].append([arr[i], arr[i+1]])
            minDiff = min(minDiff, diff)
        return dicDiff[minDiff]

class Solution2:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float('inf')
        ans = []
        arr.sort()
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            curr_arr = [arr[i-1], arr[i]]
            if diff < minDiff:
                minDiff = diff
                ans = [curr_arr]
            elif diff == minDiff:
                ans.append(curr_arr)
        return ans
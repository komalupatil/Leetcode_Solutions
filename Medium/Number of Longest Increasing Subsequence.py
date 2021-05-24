#Leetcode 673. Number of Longest Increasing Subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        # Build a tree structure linking indices of previous smaller number to subsequent larger number.
        # Use a list of list to store this "index tree" structure.
        tree = []
        q0 = set(range(n))  # q0 stores the root nodes of trees
        for i in range(n-1):
            temp = []
            j = i + 1
            while j <= n - 1:
                if nums[j] > nums[i]: 
                    temp.append(j)
                    while j < n - 1 and nums[j+1] > nums[j]: j += 1
                j += 1
            tree.append(temp)
            q0 -= set(tree[-1])  # Once an index is linked to previous indices, it is no longer a root node.
        tree.append([])
        
        # Do layer-by-layer BFS of the index tree. 
        # The longest increasing subsequences sit in the last layer.
        # Use a dictionary structure to store the # of ways to link to a certain node.
        q = {_:1 for _ in q0}
        while q:
            ans = sum(q[_] for _ in q)
            temp_q = {}
            for i in q:
                for new_i in tree[i]:
                    if new_i not in temp_q: temp_q[new_i] = q[i]
                    else: temp_q[new_i] += q[i]
            q = temp_q
        return an
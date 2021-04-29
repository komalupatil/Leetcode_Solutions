#Leetcode 938. Range Sum of BST

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s = 0
        if root == None:
            return s
        
        if low <= root.val <= high:
            s += root.val
        
        s += self.rangeSumBST(root.left, low, high)
        s += self.rangeSumBST(root.right, low, high)
        
        return s


#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s = 0
        if root == None:
            return s
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if low <= node.val <= high:
                s += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return s
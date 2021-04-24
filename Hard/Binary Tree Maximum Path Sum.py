#Leetcode 124. Binary Tree Maximum Path Sum


#Solution
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
    
        self.maxpathSum = float('-inf')
        
        def depth(node):
            
            if node == None:
                return 0
            
            left = max(0, depth(node.left))
            right = max(0, depth(node.right))
            currentmaxPath=node.val+left+right
            self.maxpathSum = max(self.maxpathSum, currentmaxPath)

            return (max(left,right) + node.val)
        depth(root)
        return self.maxpathSum
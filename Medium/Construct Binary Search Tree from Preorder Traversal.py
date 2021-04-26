#Leetocde 1008. Construct Binary Search Tree from Preorder Traversal

#Solution1 - recursion
#Convert preorder into inorder by sorting it. then find the index root in inorder and do the recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        inorder = sorted(preorder)      
        return self.helper(preorder, inorder)
    
    def helper(self, preorder, inorder):
        
        lengthPre = len(preorder)
        lengthIn = len(inorder)
        
        if lengthPre != lengthIn or preorder == None or inorder==None or lengthPre == 0:
            return None
        
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        
        root.left = self.helper(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.helper(preorder[rootIndex+1:], inorder[rootIndex+1:])   
        return root

#SOlution2 - Interative approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])       
        stack = [root]
        
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val <value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)               
        return root


#SOlution3 - recursive without converting to inorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    index = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        return self.helper(preorder,bound=float('inf'))
            
    def helper(self, A, bound=float('inf')):
        if self.index == len(A) or A[self.index] > bound:
            return None
        root = TreeNode(A[self.index])
        self.index += 1
        root.left = self.helper(A, root.val)
        root.right = self.helper(A, bound)
        return root
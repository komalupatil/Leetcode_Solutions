#Leetcode 449. Serialize and Deserialize BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        

        def preOrder(node, values):
            if node:
                values = values + str(node.val) + ','
                values = preOrder(node.left, values)
                values = preOrder(node.right, values)
            return values

        return preOrder(root, "")

        

    def deserialize(self, data: str) -> TreeNode:
        vals = collections.deque(int(val) for val in data.split(',') if val != "")

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
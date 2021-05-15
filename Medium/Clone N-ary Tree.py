#Leetcode 1490. Clone N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        visited = {}
        
        queue = deque()
        queue.append(root)
        visited[root] = Node(root.val)
        
        while queue:
            node = queue.popleft()
            for child in node.children:
                if child not in visited:
                    visited[child] = Node(child.val)
                    queue.append(child)
                visited[node].children.append(visited[child])
        return visited[root]
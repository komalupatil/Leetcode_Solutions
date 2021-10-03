#Leetcode 490. The Maze

#BFS Approach
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not start or not destination:
            return False
        if start == destination:
            return True
        
        m = len(maze)
        n = len(maze[0])
        
        q = deque([(start[0], start[1])])
        visited = set()
        directions = ([0,1], [0,-1], [1,0], [-1,0])
        
        while q:
            current = q.popleft()
            
            if current[0] == destination[0] and current[1] == destination[1]:
                return True
            
            for d in directions:
                x = current[0] + d[0]
                y = current[1] + d[1]
                
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                x -= d[0]
                y -= d[1]
                
                if (x,y) not in visited:
                    visited.add((x,y))
                    q.append([x,y])
                
        return False 

#DFS Approach

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        directions = ([0,1], [0,-1], [1,0], [-1,0])
        
        def dfs(x,y):
            
            if (x,y) in visited:
                return False
            visited.add((x,y))
            
            if [x, y] == destination:
                return True
            
            for d in directions:
                newX = x
                newY = y
                while 0 <= newX+d[0] < m and 0 <= newY+d[1] < n and maze[newX+d[0]][newY+d[1]] != 1:
                    newX += d[0]
                    newY += d[1]
                if dfs(newX, newY):
                    return True
            
            return False
        return dfs(*start)
#Leetcode 505. The Maze II

from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        if start == destination:
            return 0
        m = len(maze)
        n = len(maze[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        q = deque([tuple(start + [0])])
        visited = {tuple(start): 0}
        res = []
        
        while q:
            prev_x, prev_y, prev_dist = q.popleft()
            for d in directions:
                x,y,dist = prev_x, prev_y, prev_dist
                while 0 <= x+d[0] < m and 0 <= y+d[1] < n and maze[x+d[0]][y+d[1]] == 0:
                    dist += 1
                    x += d[0]
                    y += d[1]
                if [x,y] == destination:
                    res.append(dist)
                    continue
                if ((x,y) in visited and visited[(x,y)] > dist) or (x,y) not in visited:
                    visited[(x,y)] = dist
                    q.append((x,y,dist))
                    
        return min(res) if res else -1
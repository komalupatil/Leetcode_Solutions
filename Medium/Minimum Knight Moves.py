#Leetcode 1197. Minimum Knight Moves

import collections
class Solution1:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), \
                           (-1, -2), (-2, -1), (1, -2), (2, -1)]
        
        que = collections.deque([[0, 0, 0]])
        visited = {(0, 0): True}
        while que:
            x, y, d = que.popleft()
            if x == tx and y == ty:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not visited.get((nx, ny), False):
                    visited[(nx, ny)] = True
                    que.append([nx, ny, d + 1])

class Solution2:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), \
                           (-1, -2), (-2, -1), (1, -2), (2, -1)]
        tx = abs(tx)
        ty = abs(ty)
        
        que = collections.deque([[0, 0, 0]])
        visited = set()
        visited.add("0,0")
        while que:
            x, y, d = que.popleft()
            if x == tx and y == ty:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                s = str(nx) + "," + str(ny)
                if s not in visited and nx >= -2 and ny >=-2:
                    visited.add(s)
                    que.append([nx, ny, d + 1])

class Solution3:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), \
                           (-1, -2), (-2, -1), (1, -2), (2, -1)]
        tx = abs(tx)
        ty = abs(ty)
        
        que = collections.deque([[0, 0, 0]])
        visited = {(0, 0): True}
        while que:
            x, y, d = que.popleft()
            if x == tx and y == ty:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not visited.get((nx, ny), False) and nx >= -2 and ny >=-2:
                    visited[(nx, ny)] = True
                    que.append([nx, ny, d + 1])
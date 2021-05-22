#Leetcode 1079. Letter Tile Possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count  = [0]
        seen = set()
        buffer = []
        
        self.dfs(tiles, seen, buffer, count)
        return count[0]
    
    def dfs(self, tiles, seen, buffer, count):
        if len(buffer) > 0:
            count[0] += 1
 
        visited = set()

        for i in range(len(tiles)):
            if i not in seen and tiles[i] not in visited:
                seen.add(i)
                visited.add(tiles[i])
                buffer.append(tiles[i])
                self.dfs(tiles, seen, buffer, count)
                seen.remove(i)
                buffer.pop()
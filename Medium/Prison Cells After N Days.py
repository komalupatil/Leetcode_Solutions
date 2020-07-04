#Leetcode 957. Prison Cells After N Days

#Solution

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        found_cycle = {}
            
        for i in range(N):
            cells_str = str(cells)
                
            if cells_str in found_cycle:
                cycle_len = i - found_cycle[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % cycle_len)
                
            else:
                found_cycle[cells_str] = i
                cells = self.cell_values(cells)
                    
        return cells
        
    def cell_values(self, cells):
        result = [0] * 8
        for i in range(1,7):
            result[i] = int(cells[i-1]==cells[i+1])
        return result
        
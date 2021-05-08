#Leetcode 657. Robot Return to Origin

class Solution1:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        

class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U':
                x +=1
            if move == 'D':
                x -= 1
            if move == 'L':
                y += 1
            if move == 'R':
                y -= 1
        return x== y == 0
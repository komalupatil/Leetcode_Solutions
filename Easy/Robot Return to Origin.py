#Leetcode 657. Robot Return to Origin

#Solution1
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        

#Solution2
class Solution:
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
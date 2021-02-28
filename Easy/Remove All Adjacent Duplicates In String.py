#leetcode 1047. Remove All Adjacent Duplicates In String

#solution1

class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S)-1:
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                if i > 0:
                    i -=2
                else:
                    i -=1
            i +=1
        return S

#solution2

class Solution:
    def removeDuplicates(self, S: str) -> str:
        dout = []
        for s in S:
            if dout and s == dout[-1]:
                dout.pop()
            else:
                dout.append(s)
        return "".join(dout)

#Solution 3

class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        
        for i in S:
            if not res:
                res.append(i)
            else:
                if res[-1] == i:
                    del res[-1]
                else:
                    res.append(i)
        return "".join(res)

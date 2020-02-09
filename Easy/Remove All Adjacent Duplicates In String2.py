class Solution:
    def removeDuplicates(self, S: str) -> str:
        dout = []
        for s in S:
            if dout and s == dout[-1]:
                dout.pop()
            else:
                dout.append(s)
        return "".join(dout)
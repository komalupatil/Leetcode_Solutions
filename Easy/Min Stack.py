#leetcode155 Min Stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = [] 

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))
    
        

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q)-1][0]
            
        

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q)-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

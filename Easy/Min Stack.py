#leetcode155 Min Stack

#Solution1

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



#Solution2 - using two stacks 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack)==0 or x <= self.minStack[-1]:
            self.minStack.append(x)
                
    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.minStack[-1]:
            self.minStack.pop()
               
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
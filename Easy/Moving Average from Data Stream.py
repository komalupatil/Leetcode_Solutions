#Leetcode 346. Moving Average from Data Stream

#Given a stream of integers and a window size,
#calculate the moving average of all integers in the sliding window

#Solution1
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.array = []
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.array.append(val)
        if len(self.array) > self.size:
            self.sum -= self.array.pop(0)
        return self.sum/len(self.array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



#Solution2 Using deque from collections module python

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.two_way_queue = collections.deque(maxlen=size)
        
    def next(self, val: int) -> float:
        
       
        queue = self.two_way_queue
        queue.append(val)
        return float(sum(queue))/len(queue)
        
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

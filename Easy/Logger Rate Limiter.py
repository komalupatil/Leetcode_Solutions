#Leetocde 359. Logger Rate Limiter


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.d and timestamp - self.d[message] < 10:
            return False
        else:
            self.d[message] = timestamp
            return True
            
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

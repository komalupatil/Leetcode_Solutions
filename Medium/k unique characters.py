#CoderByte medium
#Find the longest substring of a string containing `k` distinct characters
#string = "3abcbdbdbbdcdabd" where string[0] is k
#For k = 2, o/p is ‘bdbdbbd’
#For k = 3, o/p is ‘bcbdbdbbdcd’

#Approach : Sliding Window
class Solution:
    def kUniqueCharacters(self, str):
        if len(str) == 0 or str == None:
            return 0
        
        windowStart = 1
        maxWindow = ""
        maxWindowStart = 0
        maxLength = float('-inf')
        
        d = {}
        k = int(str[0])

        for windowEnd in range(1, len(str)):
            rightChar = str[windowEnd]
            d[rightChar] = d.get(rightChar, 0) + 1

            while len(d) > k:
                d[str[windowStart]] -= 1
                if d[str[windowStart]] == 0:
                    del d[str[windowStart]]
                windowStart +=1
            
            if windowEnd-windowStart+1 > maxLength:
                    maxLength = windowEnd - windowStart + 1
                    maxWindowStart = max(windowStart, maxWindowStart)

        maxWindow = str[maxWindowStart:maxWindowStart+maxLength]
        return maxWindow

out = Solution()
str1 = "3abcbdbdbbdcdabd"
output1 = out.kUniqueCharacters(str1)
print(output1)



        


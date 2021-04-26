#Leetcode 728. Self Dividing Numbers

#Solution1
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result= []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            s = True
            for j in str(i):
                if i % int(j) != 0:
                    s = False
                    break
            if s == True:
                result.append(i)
        return result



#Solution2
def is_self_dividing(x):
        s = str(x)
        for i in s:
            if i=="0" or x%int(i)!=0:
                return False
        return True
class Solution:
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            if is_self_dividing(num):
                result.append(num)
        return result
                

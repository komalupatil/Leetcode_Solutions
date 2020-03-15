#leetcode 1281. Subtract the Product and Sum of Digits of an Integer
#solution1

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0:
            return 0
        product = 1
        addition = 0
        
        for i in str(n):  # here can also use function repr() instead of str() which takes less time 
            product *= int(i)
            addition += int(i)
        return product - addition



#Solution2 using map function

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n))) #this will cereate sequencedobject (list in this case)  out of returned map object (through map function) and hence can be consumed multiple times
        # B = map(int, str(n))  #this can be only consumed once, since it return a map object and that map object is then used to iterate over items
        #map function here converts each element of string format of an integer n to an int element of a list
        return reduce(operator.mul, A) - sum(A) #reduce function applied function passed (operator.mul in this case)in it to all the elements of the sequence passed (A in this case)

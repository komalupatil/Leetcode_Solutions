#Leetcode 844. Backspace String Compare

class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def bsString(string):
            result = []
            
            for c in string:
                if c != "#":
                    result.append(c)
                else:
                    result = result[:-1]
            return result
        return bsString(S) == bsString(T)

class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        indexS, indexT = len(S)-1, len(T)-1
        countS = countT = 0
        while indexS >=0 or indexT >=0:
            
            while indexS >=0:
                
                if S[indexS] == "#":
                    countS +=1
                    indexS -=1
                elif countS >0:
                    countS -=1
                    indexS -=1
                else:
                    break
        
        
            while indexT >=0:
                
                if T[indexT] == "#":
                    countT +=1
                    indexT -=1
                elif countT >0:
                    countT -=1
                    indexT -=1
                else:
                    break
            
            if indexS < 0  and indexT <0:
                return True
            
            if indexS < 0  or indexT <0:
                    return False
                
            if S[indexS] != T[indexT]:
                return False
                    
            
            indexS -=1
            indexT -=1
            
        return True
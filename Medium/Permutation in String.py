#Leetcode 567. Permutation in String

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
    
        target = [0] * 26
        for x in A:
            target[x] += 1
    
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        length_of_s1  = len(s1)
        s1_counter = Counter(s1)
        window_counter = Counter()
        
        for i,ch in enumerate(s2):
            window_counter[ch] +=1
            
            if i>= length_of_s1:
                eliminate_from_left = s2[i-length_of_s1]
            
                if window_counter[eliminate_from_left] == 1:
                    del window_counter[eliminate_from_left]
                else:
                    window_counter[eliminate_from_left] -=1
            
            if window_counter == s1_counter:
                return True
        return False
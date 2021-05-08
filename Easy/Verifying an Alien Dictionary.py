#Leetcode 953. Verifying an Alien Dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return true
        
        new_words = []
        
        order = {c: i for i,c in enumerate(order)}
        
        for w in words:
            new = []
            for c in w:
                #Transform the list of words into its index in new order.
                new.append(order[c])
            new_words.append(new)
        
        #For list comparision, if we want w1 < w2, if len(w1) = len(w2), it will compare each element in w1/w2, if everyone successes, return True.
        #If len is different. then if len(w1) > len(w2): it will return false since null is less than anything. if len(w1) < len(w2), then as long as everyone in w1 is less than its corresponding cmpoent in w2, it will return True.
        #This is the same as lexicographicaly sort.
        #if w1 > w2: since testcase is missing duplicates in the list, so to handle duplicate, we use > instead of >=
        for i in range(len(new_words)-1):
            if new_words[i] > new_words[i+1]:
                return False
        return True
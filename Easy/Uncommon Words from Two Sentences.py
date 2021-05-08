#Leetcode 884. Uncommon Words from Two Sentences

class Solution1:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dicti = {}
        listi = []
        A_B_str = A + " " + B
        A_B_list = A_B_str.split(" ")
        for i in range(len(A_B_list)):
            if A_B_list[i] in dicti.keys():
                dicti[A_B_list[i]] +=1
            else:
                dicti[A_B_list[i]] = 1
        for k,v in dicti.items():
            if v == 1:
                listi.append(k)
        return listi


class Solution2:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = {}
        
        for i in A.split():
            d[i] = d.get(i,0)+1
        for j in B.split():
            d[j] = d.get(j, 0)+1
        
        return [word for word in d if d[word] == 1]
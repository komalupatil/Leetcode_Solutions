class Solution:
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
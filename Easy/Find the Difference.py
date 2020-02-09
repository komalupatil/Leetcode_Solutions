class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicti = {}
        for i in range(len(s)):
            if s[i] in dicti.keys():
                dicti[s[i]] += 1
            else:
                dicti[s[i]] = 1
        for j in range(len(t)):
            if t[j] in dicti.keys():
                dicti[t[j]] -= 1
            else:
                dicti[t[j]] = 1
        for k,v in dicti.items():
            if v != 0:
                return k
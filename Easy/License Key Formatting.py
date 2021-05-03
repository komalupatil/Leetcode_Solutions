#Leetcode 482. License Key Formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')[::-1]
        S = []
        for i in range(0, len(s), k):
            S.append(s[i:i+k])
        return '-'.join(S)[::-1]
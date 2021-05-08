#Leetcode 49. Group Anagrams

#using dictionary of lists
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            d[tuple(count)].append(string)
        return d.values()
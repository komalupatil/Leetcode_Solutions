#Leetcode 1436. Destination City

class Solution1:
    def destCity(self, paths: List[List[str]]) -> str:
        d= {}
        for path in paths:
            a, b = path
            if a not in d.keys():
                d[a] = b
        for val in d.values():
            if val not in d.keys():
                return val

class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set(path[0] for path in paths)
        for path in paths:
            if path[1] not in s:
                return path[1]
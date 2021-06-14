#Leetcode 207. Course Schedule

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return False
        
        sortedOrder = []
        inDegree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        for prereq in prerequisites:
            parent, child = prereq[0], prereq[1]
            graph[parent].append(child)
            inDegree[child] += 1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        return len(sortedOrder) == numCourses
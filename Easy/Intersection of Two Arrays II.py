#Leetcode 350. Intersection of Two Arrays II

#Solution1  - sorted

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i,j=0,0
        while i< len(nums1) and j< len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                result.append(nums1[i])
                i+=1
                j+=1
        return result
        

#Solution2 - using dictionary

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        result = []
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                result.append(i)
                dict1[i] -= 1
        return result
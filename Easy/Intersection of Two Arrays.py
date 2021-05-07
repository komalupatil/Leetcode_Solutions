#Leetcode 349. Intersection of Two Arrays

class Solution1:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)



class Solution2:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dicti = {}
        listi = []
        for i in range(len(nums1)):
            if nums1[i] in dicti.keys():
                dicti[nums1[i]] += 1
                continue
            else:
                dicti[nums1[i]] = 1

        for j in range(len(nums2)):
            if nums2[j] in dicti.keys():
                if nums2[j] not in listi:
                    listi.append(nums2[j])

        return listi

    
class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        d = {}
        
        for i in nums1:
            d[i] = d.get(i,0)+1
        for j in nums2:
            if j in d and d[j] >0:
                result.append(j)
                d[j] = 0
        return result


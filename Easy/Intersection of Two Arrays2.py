class Solution:
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
        print(dicti)

        for j in range(len(nums2)):
            if nums2[j] in dicti.keys():
                if nums2[j] not in listi:
                    listi.append(nums2[j])

        return listi



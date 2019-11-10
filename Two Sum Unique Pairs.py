class Uniquepairs:
    def TwoSumUniquePairs(self, nums, target):
        nums.sort()
        i, j = 0, len(nums)-1
        result = 0
        while i < j:
            if nums[i] + nums[j] < target:
                i +=1
            elif (nums[i] + nums[j]) > target:
                j -=1
            else:
                result +=1
                i +=1
                j -=1
                while (i < j and nums[i] == nums[i-1]):
                    i +=1
                while(i < j and nums[j] == nums[j+1]):
                    j -=1
        return result
    

uniquepairs = Uniquepairs()
nums1 = [1,1,2,45,46,46]
target1 = 47
nums2 = [1,1]
target2 = 2
nums3 = [1,5,1,5]
target3 = 6
result1 = uniquepairs.TwoSumUniquePairs(nums1, target1)
result2 = uniquepairs.TwoSumUniquePairs(nums2, target2)
result3 = uniquepairs.TwoSumUniquePairs(nums3, target3)
print(result1)
print(result2)
print(result3)

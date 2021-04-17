#Leetcode 26. Remove Duplicates from Sorted Array 

#Solution
class removeduplicates:
    def rem_dup(self, nums):
        slow = 0 #slow pointer
        fast = 1 #fast pointer
        while(fast< len(nums)):
            if nums[slow] != nums[fast]:
                slow +=1 
                nums[slow] = nums[fast]
            else:
                fast +=1
        return slow+1 #takes only the length of actual non duplicate numbers


nums1 = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates = removeduplicates()
result = removeDuplicates.rem_dup(nums1)
print(result)
print(nums1[0:result])

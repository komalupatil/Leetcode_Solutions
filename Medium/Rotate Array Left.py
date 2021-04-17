#similar to leetcode 189 Rotate array (rotating to the left instead of right)

#solution1
#using list indexing
def rotate_array_left(nums, k):
    k = k%len(nums)
    nums[:] = nums[len(nums)-k-1:] + nums[:k]
    return nums
def main():
    nums1=[1,2,3,4,5,6,7]
    k1=3
    result= rotate_array_left(nums1, k1)
    print(result)
main()
    


#solution2
#using reverse function
class Solution:
    
    def rev(self,nums,s,e):
        while(s<e):
            temp = nums[s]
            nums[s] = nums[e]
            nums[e] = temp
            s +=1
            e -=1

    def rotate_array_left(self,nums,k):
        k = k% len(nums)
        self.rev(nums,0,k-1)
        self.rev(nums, k, len(nums)-1)
        self.rev(nums, 0, len(nums)-1)
        return nums
solution = Solution()
nums1=[1,2,3,4,5,6,7]
k1=3
result = solution.rotate_array_left(nums1,k1)
print(result)

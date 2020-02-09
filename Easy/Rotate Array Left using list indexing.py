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
    

#reverse elements of an array
def rev(nums, s,e):
    while (s < e):
        temp = nums[s]
        nums[s] = nums[e]
        nums[e] = temp
        s +=1
        e -=1
    return nums
def main():
    nums1 = [1,2,3,4,5,6,7,8,9]
    s1 = 0
    e1 = len(nums1)-1
    result = rev(nums1, s1, e1)
    print(result)
main()
    

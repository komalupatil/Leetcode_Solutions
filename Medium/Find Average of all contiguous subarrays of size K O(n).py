#avg of contiguous subarrays of size k optimal O(n)

def avg_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1 :
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart +=1
    return result

def main():
    K1 = 4
    arr1 = [2,3,4,6,-1,9,-4,3]
    result = avg_of_subarrays(K1, arr1)
    print("Avgs of subarrays of size K is: " + str(result))
main()
            

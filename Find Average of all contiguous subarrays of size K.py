#Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

def avg_of_subarrays(K, arr):
    result= []
    for i in range(len(arr)-K+1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
        result.append(sum/K)
    return result
def main():
    K1 = 4
    arr1 = [2,3,4,6,-1,9,-4,3]
    result = avg_of_subarrays(K1, arr1)
    print("Avgs of subarrays of size K is: " + str(result))
main()
    

        
        

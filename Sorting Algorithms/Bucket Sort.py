#Solution1 - for fractional numbers only

class Sort:
    def insertionSort(Self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    def bucketSort(self, arr):
        buckets = []

        for num in range(len(arr)):
            buckets.append([])

        for i in arr:
            bucket_index = int(len(arr)*i)
            buckets[bucket_index].append(i)

        for j in range(len(arr)):
            buckets[j] = self.insertionSort(buckets[j])

        k=0
        for i in range(len(arr)):
            for j in range(len(buckets[i])):
                arr[k] = buckets[i][j]
                k+=1
        return arr

obj = Sort()
arr1 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
sortedArray = obj.bucketSort(arr1)
print(sortedArray)

#Solution2 - for fractional or integers

class Sort:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def bucketSort(self,arr):
        largest = max(arr)
        size = largest/len(arr)

        buckets = []

        for _ in range(len(arr)):
            buckets.append([])
        
        for i in range(len(arr)):
            j = int(arr[i]/size)
            if j != len(arr):
                buckets[j].append(arr[i])
            else:
                buckets[len(arr)-1].append(arr[i])

        for i in range(len(arr)):
            self.insertionSort(buckets[i])
        
        k = 0

        for i in range(len(arr)):
            for j in range(len(buckets[i])):
                arr[k] = buckets[i][j]
                k +=1
        return arr

obj = Sort()
arr2 = [12,11,13,5,6]
sortedArray = obj.insertionSort(arr2)
print(sortedArray)


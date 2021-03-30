#Solution 1
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
obj = Sort()
arr1=[12,11,13,5,6]
sortedArray = obj.insertionSort(arr1)
print(sortedArray)

#Solution 2
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        value_to_sort = sequence[i]
        while sequence[i-1] > value_to_sort and i>0:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i = i-1
    return sequence

print(insertion_sort([12,11,13,5,6]))



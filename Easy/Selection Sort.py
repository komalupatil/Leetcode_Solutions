#Selection Sort Algorithm

def Selection_sort(sequence):
    for i in range(0, len(sequence)-1):
        min_value = i

        for j in range(i, len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j
        
        if min_value != i:
            sequence[min_value], sequence[i] = sequence[i], sequence[min_value]
        
    
    return sequence


print(Selection_sort([5,6,2,1,0,7,5,4,3,9,0]))
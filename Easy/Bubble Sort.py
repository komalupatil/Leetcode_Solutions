#Bubble Sort Algorithm

def bubble_sort(sequence):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                sorted = False
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    return sequence

print(bubble_sort([7,4,3,5,8,9,0,2,3,1]))
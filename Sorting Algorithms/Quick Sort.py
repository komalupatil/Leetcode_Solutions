def quick_sort(sequence):
    s = len(sequence) 
    if s <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater_than_pivot = []
    items_less_than_pivot = []

    for item in sequence:
        if item > pivot:
            items_greater_than_pivot.append(item)
        else:
            items_less_than_pivot.append(item)
    return quick_sort(items_less_than_pivot) + [pivot] + quick_sort(items_greater_than_pivot)

print(quick_sort([5,3,8,6,1,0,9,2]))

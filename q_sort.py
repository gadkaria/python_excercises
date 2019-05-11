#!/usr/bin/env python3

# helper function that moves values around 
def partition(array, start, end):
    # Many ways to chose pivot, will choose middle of the array
    pivot = end

    i = start -1

    # Linear search through the array to place things on the correct side of the pivot
    for j in range(start,end):
        if array[j] <= array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]

    #swap the pivot in to its correct place 
    array[i+1], array[pivot] = array[pivot], array[i+1]
    return i+1


# recursive fucntion that sorts the array
def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)

        # recursively call quick sort on the left half of the array
        quickSort(array, start, pivot-1)

        # right half of the array
        quickSort(array, pivot + 1, end)

# test function 
def main():
    test = [3,6,2,14,8,10,4]
    quickSort(test, 0, len(test)-1)
    print(test)

main()

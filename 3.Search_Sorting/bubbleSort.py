"""If you were to perform a bubble sort ob the following array, what would the
third iteration look like,
[21, 4, 1, 3, 9, 20, 25, 6, 21, 14]"""
from random import randint


def bubbleSort(input_list, iteration):
    # O(N^2)
    while iteration > 0:
        for i in range(len(input_list) - 1):
            first = input_list[i]
            second = input_list[i + 1]
            if first > second:
                input_list[i] = second
                input_list[i + 1] = first
        print(iteration, " iteration results is ", input_list)
        iteration -= 1


def mergeSort(arr):
    # O(n*log(n))
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


# seq = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# bubbleSort(seq, 3)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(mergeSort(test))
print(quickSort(test, 0, 9))

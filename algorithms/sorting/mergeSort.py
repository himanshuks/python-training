# Merge sort function is given below
# This will break the array into smaller chunks
# Such a way that each element is an array having only one element
def merge_sort(arr):

    # Return when array size is equal to 1 while dividing them
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Break current array into LEFT and RIGHT partition
    left = arr[:mid]
    right = arr[mid:]

    # Break the LEFT and RIGHT partition further more using recursion
    merge_sort(left)
    merge_sort(right)

    # Once individual array is created, start merging them
    merge_sorted_array(left, right, arr)


# This will merge two small sorted array
def merge_sorted_array(a, b, arr):
    print(f"Merge called : Left {a} Right {b} Array {arr}")

    # Getting started with single container array
    # Left and Right is passed along with main array
    # Main array is not a list of arrays for understanding
    # Arr = [['A'],['B'],['C'],['D']]

    len_a = len(a)
    len_b = len(b)

    # Three pointers will point START of array A, B and ARR respectively
    i = j = k = 0

    # Compare A and B and assign element in ARR in increasing order
    # Also move the pointer by 1
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1

    # Take extra elements from A if size is bigger than B
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    # Take extra elements from B if size is bigger than A
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


a = [5, 8, 12, 58]
b = [7, 9, 45, 51]

arr = [10, 3, 15, 7, 8, 23, 98, 29]

# x = merge_sorted_array(a, b)
# print(x)
print("Before sort:", arr)
merge_sort(arr)
print("\nSorted array by MERGE:", arr)
